from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class FactoryMachine(Base):
    __tablename__ = "factory_machines"

    id = Column(Integer, primary_key=True, index=True)
    machine_name = Column(String, unique=True, index=True)
    status = Column(String, default="Stopped")
    production_count = Column(Integer, default=0)
    
    # New Textile Columns 🔥
    yarn_count = Column(Integer, default=0)
    efficiency = Column(Float, default=0.0)
    pick_density = Column(Integer, default=0)
    production_meters = Column(Integer, default=0)
    temperature = Column(Float, default=0.0)
    ph_level = Column(Float, default=0.0)
