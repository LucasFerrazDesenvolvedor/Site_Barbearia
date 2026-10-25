from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import Base, engine
from app.api.v1.router import api_router
from app.models import Service, Barber
from app.database import SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/api/v1/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def seed_initial_data():
    db = SessionLocal()
    try:
        if not db.query(Service).first():
            db.add_all([
                Service(name="Corte Degradê / Social", price=35.0, duration_minutes=30, description="Acabamento impecável com navalha e lavagem"),
                Service(name="Barba Completa", price=25.0, duration_minutes=25, description="Toalha quente, alinhamento e óleo hidratante"),
                Service(name="Combo Corte + Barba", price=55.0, duration_minutes=55, description="Experiência completa para o seu visual"),
                Service(name="Sobrancelha na Navalha", price=12.0, duration_minutes=10, description="Design masculino rápido e limpo"),
                Service(name="Pigmentação de Barba", price=30.0, duration_minutes=20, description="Correção de falhas com tinta profissional")
            ])
        if not db.query(Barber).first():
            db.add_all([
                Barber(name="Matheus do Corte", phone="5583999991111"),
                Barber(name="Lucas Navalha", phone="5583999992222"),
                Barber(name="Felipe Faded", phone="5583999993333")
            ])
        db.commit()
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API Barbearia Matheus do Corte rodando com sucesso!", "docs": "/docs"}