from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from datetime import datetime
from app.api.deps import get_db
from app.models import Appointment, Barber, Service
from app.schemas.appointment import AppointmentCreate, AppointmentResponse
from app.services.whatsapp import send_whatsapp_confirmation

router = APIRouter()

@router.get("/", response_model=list[AppointmentResponse])
def list_appointments(date: str | None = None, db: Session = Depends(get_db)):
    query = db.query(Appointment)
    if date:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        query = query.filter(Appointment.appointment_date >= target_date)
    return query.order_by(Appointment.appointment_date.asc()).all()

@router.post("/", response_model=AppointmentResponse, status_code=201)
def create_appointment(
    appointment_in: AppointmentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    barber = db.query(Barber).filter(Barber.id == appointment_in.barber_id).first()
    if not barber:
        raise HTTPException(status_code=404, detail="Barbeiro não encontrado.")

    services = db.query(Service).filter(Service.id.in_(appointment_in.service_ids)).all()
    if not services:
        raise HTTPException(status_code=400, detail="Selecione ao menos um serviço válido.")

    # Conflito de horário
    existing = db.query(Appointment).filter(
        Appointment.barber_id == appointment_in.barber_id,
        Appointment.appointment_date == appointment_in.appointment_date,
        Appointment.status != "CANCELLED"
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Horário já ocupado para este barbeiro.")

    total_price = sum(s.price for s in services)

    appointment = Appointment(
        client_name=appointment_in.client_name,
        client_phone=appointment_in.client_phone,
        appointment_date=appointment_in.appointment_date,
        barber_id=appointment_in.barber_id,
        services=services,
        total_price=total_price,
        status="CONFIRMED"
    )

    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    # Notificação assíncrona
    services_names = ", ".join([s.name for s in services])
    date_formatted = appointment.appointment_date.strftime("%d/%m/%Y às %H:%M")
    msg = f"Fala {appointment.client_name}! Seu agendamento na Barbearia Matheus do Corte foi confirmado para {date_formatted} ({services_names}) com {barber.name}."
    background_tasks.add_task(send_whatsapp_confirmation, appointment.client_phone, msg)

    return appointment