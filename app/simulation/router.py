from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.simulation.models import FactoryMachine
import random

# Yeh hai woh 'router' jo main.py dhoond rahi hai!
router = APIRouter(
    prefix="/simulation",
    tags=["Industrial Simulation Engine"]
)

# Route 1: Saari live machines ka data dekhne ke liye
@router.get("/status")
def get_factory_status(db: Session = Depends(get_db)):
    return db.query(FactoryMachine).all()

# Route 2: Hackathon Special - Live data mock karne ke liye
@router.post("/trigger-mock-telemetry")
def trigger_telemetry(db: Session = Depends(get_db)):
    machines = ["Boiler-X1", "Assembly-Line-04", "Robotic-Arm-Alpha"]
    
    for name in machines:
        machine = db.query(FactoryMachine).filter(FactoryMachine.machine_name == name).first()
        if not machine:
            machine = FactoryMachine(machine_name=name)
            db.add(machine)
        
        # Industry level random numbers simulate kar rahe hain
        machine.temperature = round(random.uniform(65.0, 120.5), 2)
        machine.production_count += random.randint(5, 25)
        machine.status = "Running" if machine.temperature < 105 else "Critical Overheat"
        
    db.commit()
    return {"message": "Factory metrics successfully simulated!", "status": "Success"}
