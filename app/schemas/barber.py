from pydantic import BaseModel

class BarberBase(BaseModel):
    name: str
    phone: str | None = None
    avatar_url: str | None = None

class BarberCreate(BarberBase):
    pass

class BarberResponse(BarberBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True