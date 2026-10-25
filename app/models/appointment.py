from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

appointment_services = Table(
    "appointment_services",
    Base.metadata,
    Column("appointment_id", Integer, ForeignKey("appointments.id", ondelete="CASCADE"), primary_key=True),
    Column("service_id", Integer, ForeignKey("services.id", ondelete="CASCADE"), primary_key=True)
)

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(100), nullable=False)
    client_phone = Column(String(20), nullable=False)
    appointment_date = Column(DateTime, nullable=False, index=True)
    status = Column(String(20), default="PENDING")  # PENDING, CONFIRMED, CANCELLED, COMPLETED
    total_price = Column(Float, nullable=False)
    
    barber_id = Column(Integer, ForeignKey("barbers.id"), nullable=False)
    barber = relationship("Barber", back_populates="appointments")
    
    services = relationship("Service", secondary=appointment_services, back_populates="appointments")