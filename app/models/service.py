from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    duration_minutes = Column(Integer, nullable=False, default=30)
    is_active = Column(Boolean, default=True)

    appointments = relationship("Appointment", secondary="appointment_services", back_populates="services")