from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class FactoryMachine(Base):
    __tablename__ = "factory_machines"

    id = Column(Integer, primary_key=True, index=True)
    machine_name = Column(String, index=True)       # e.g., "Boiler-01", "CNC-Machine"
    status = Column(String, default="Operational")  # e.g., Running, Idle, Maintenance
    temperature = Column(Float, nullable=True)      # Live Temperature in Celsius
    production_count = Column(Integer, default=0)   # Total items produced
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
