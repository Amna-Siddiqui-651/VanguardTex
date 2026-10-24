from fastapi import FastAPI
from app.database import engine, Base
from app.simulation.router import router as simulation_router
from app.auth.router import router as auth_router  # <-- Naya Auth Router Import

# Create Database Tables Automatically (Ab automatic users ka table bhi banega!)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VanguardTex Industrial Simulation Platform",
    description="Enterprise-grade smart factory live telemetry and automation API.",
    version="1.0.0"
)

# Saare modules ko yahan register kar rahe hain
app.include_router(auth_router)        # <-- Naya Auth Module Include
app.include_router(simulation_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to VanguardTex Industrial Simulation Platform! Core engine is 100% active."}
