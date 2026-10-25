from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.barber import Barber
from app.schemas.barber import BarberCreate, BarberResponse

router = APIRouter()

@router.get("/", response_model=list[BarberResponse])
def list_barbers(db: Session = Depends(get_db)):
    return db.query(Barber).filter(Barber.is_active == True).all()

@router.post("/", response_model=BarberResponse, status_code=201)
def create_barber(barber_in: BarberCreate, db: Session = Depends(get_db)):
    barber = Barber(**barber_in.model_dump())
    db.add(barber)
    db.commit()
    db.refresh(barber)
    return barber