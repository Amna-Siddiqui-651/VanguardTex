from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.simulation.models import FactoryMachine
from app.auth.router import get_current_user
import random

router = APIRouter(
    prefix="/simulation",
    tags=["Industrial Simulation Engine"]
)

# Route 1: Trainee ya Admin apna live status dekh sakte hain
@router.get("/status")
def get_factory_status(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(FactoryMachine).all()

# Route 2: Sirf Admin/Manager hi production simulator chala sakta hai!
@router.post("/trigger-mock-telemetry")
def trigger_telemetry(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Hackathon-level Role Verification
    if current_user.role != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Access Denied: Only Admins can trigger factory simulation metrics!"
        )
        
    # Asli Textile Machines ki list
    textile_machines = ["Spinning-Frame-01", "Weaving-Loom-X", "Dyeing-Jet-Alpha"]
    
    for name in textile_machines:
        machine = db.query(FactoryMachine).filter(FactoryMachine.machine_name == name).first()
        if not machine:
            machine = FactoryMachine(machine_name=name)
            db.add(machine)
        
        # Har machine ke hisab se dynamic textile telemetry metrics generate karna
        if name == "Spinning-Frame-01":
            machine.yarn_count = random.randint(20, 40)  # Standard Yarn Count (Ne)
            machine.efficiency = round(random.uniform(85.0, 98.5), 2)
            machine.status = "Optimal Running" if machine.efficiency > 90 else "Low Efficiency Alert"
            
        elif name == "Weaving-Loom-X":
            machine.pick_density = random.randint(50, 80)  # PPI (Picks Per Inch)
            machine.production_meters = random.randint(10, 50)
            machine.status = "Weaving Premium Grade"
            
        elif name == "Dyeing-Jet-Alpha":
            machine.temperature = round(random.uniform(95.0, 135.0), 2)  # High temp dyeing
            machine.ph_level = round(random.uniform(5.5, 8.5), 2)         # Acidic/Alkaline check
            machine.status = "Dyeing Process Active" if (6.0 <= machine.ph_level <= 7.5) else "Chemical Imbalance Warning"
       
               # 🌟 ASLI BUG FIX AREA: Agar value None hai to pehle usay 0 set karein taake crash na ho!
        if machine.production_count is None:
            machine.production_count = 0
            
        machine.production_count += random.randint(5, 25)

    # 🌟 NEW ECONOMY ENGINE LOGIC START 🔥 🌟
    # 1. Deduct Factory Operating Cost
    current_user.cash -= 1000 
    
    # 2. Add Experience Points (XP)
    current_user.xp += 50
    
    # 3. Smart Level-Up Check! (Har 100 XP par level badhega)
    if current_user.xp >= (current_user.level * 100):
        current_user.level += 1
        level_up_msg = f"🏆 LEVEL UP! You are now Level {current_user.level}!"
    else:
        level_up_msg = "Keep scaling the factory!"

    db.commit() # Database mein modifications save karne ke liye
    
    return {
        "message": "Textile Smart Factory Telemetry successfully simulated by Admin!", 
        "triggered_by": current_user.username,
        "economy_report": {
            "factory_operating_cost": "- Rs. 1000",
            "current_remaining_cash": f"Rs. {current_user.cash}",
            "xp_earned": "+50 XP",
            "total_xp": f"{current_user.xp} XP",
            "level_status": level_up_msg
        },
        "status": "Success"
    }

