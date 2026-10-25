from pydantic import BaseModel
from datetime import datetime
from app.schemas.service import ServiceResponse
from app.schemas.barber import BarberResponse

class AppointmentCreate(BaseModel):
    client_name: str
    client_phone: str
    barber_id: int
    service_ids: list[int]
    appointment_date: datetime

class AppointmentResponse(BaseModel):
    id: int
    client_name: str
    client_phone: str
    appointment_date: datetime
    status: str
    total_price: float
    barber: BarberResponse
    services: list[ServiceResponse]

    class Config:
        from_attributes = True