from pydantic import BaseModel

class ServiceBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    duration_minutes: int

class ServiceCreate(ServiceBase):
    pass

class ServiceResponse(ServiceBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True