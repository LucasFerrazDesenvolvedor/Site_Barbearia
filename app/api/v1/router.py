from fastapi import APIRouter
from app.api.v1 import services, barbers, appointments

api_router = APIRouter()
api_router.include_router(services.router, prefix="/services", tags=["Serviços"])
api_router.include_router(barbers.router, prefix="/barbers", tags=["Barbeiros"])
api_router.include_router(appointments.router, prefix="/appointments", tags=["Agendamentos"])