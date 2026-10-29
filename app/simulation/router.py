from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from app.database import get_db
from app.simulation.models import FactoryMachine
from app.auth.router import get_current_user
from typing import Dict, Any
import random

router = APIRouter(
    prefix="/simulation",
    tags=["Industrial Simulation Engine"]
)

# =====================================================================
# PHASE 4 & 5: EXISTING STABLE ENDPOINTS
# =====================================================================

# Route 1: Trainee ya Admin apna live status dekh sakte hain
@router.get("/status")
def get_factory_status(db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    return db.query(FactoryMachine).all()

# Route 2: Sirf Admin/Manager hi production simulator chala sakta hai!
@router.post("/trigger-mock-telemetry")
def trigger_telemetry(db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
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

    #  NEW ECONOMY ENGINE LOGIC START  
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


# =====================================================================
# NEW PHASE 6: STANDALONE LAB LOGIC ENGINE (PREDICTIVE QUALITY ANALYZER)
# =====================================================================

# Pydantic Schema: Request payload validation ke liye
class QualityTelemetryInput(BaseModel):
    batch_number: str = Field(..., description="Unique ID for the produced fabric batch")
    target_yarn_count: float = Field(..., description="Target Yarn Count in Ne (e.g., 20.0)")
    actual_yarn_count: float = Field(..., description="Sensor measured Yarn Count from floor")
    loom_efficiency: float = Field(..., description="Current Loom Efficiency percentage (0-100)")
    target_ppi: int = Field(..., description="Target Picks Per Inch density")
    actual_ppi: int = Field(..., description="Actual Picks Per Inch measured by optic sensors")
    ph_level: float = Field(..., description="Wet finishing chemistry fluid pH level")

# Pydantic Schema: Response output structure ke liye
class LabAnalysisResponse(BaseModel):
    status: str
    batch_id: str
    fabric_grade: str
    compliance_report: Dict[str, Any]
    financials_updated: Dict[str, Any]


@router.post("/analyze-quality", response_model=LabAnalysisResponse)
def analyze_fabric_quality(
    payload: QualityTelemetryInput,
    current_user: Any = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    VanguardTex PHASE 6 - Predictive Quality Analyzer (The Lab Logic Engine):
    Runs full deterministic checks on raw textile streams to compute compliance grades
    and injects massive business rewards into the user's gamified profile.
    """
    failed_parameters = []

    # 1. Yarn Count Deviation Check (Tolerance Max 5%)
    yarn_dev = abs(payload.actual_yarn_count - payload.target_yarn_count) / payload.target_yarn_count
    if yarn_dev > 0.05:
        failed_parameters.append(f"Yarn Count Deviation High ({yarn_dev * 100:.2f}%)")

    # 2. Mechanical Loom Efficiency Check (Min 85% required for Grade A)
    if payload.loom_efficiency < 85.0:
        failed_parameters.append(f"Low Loom Efficiency Level ({payload.loom_efficiency}%)")

    # 3. Pick Density / PPI Deviation Check (Tolerance Max 3%)
    ppi_dev = abs(payload.actual_ppi - payload.target_ppi) / payload.target_ppi
    if ppi_dev > 0.03:
        failed_parameters.append(f"Pick Density Deviation High ({ppi_dev * 100:.2f}%)")

    # 4. Finishing pH Fluid Check (Must be standard neutral 6.5 - 7.5)
    if not (6.5 <= payload.ph_level <= 7.5):
        failed_parameters.append(f"Critical Chemical pH Imbalance ({payload.ph_level})")

    # --- Grading Assessment & Economic Impact Calculations ---
    if len(failed_parameters) == 0:
        final_grade = "Grade A (Export Ready)"
        cash_reward = 7500.0
        xp_reward = 200
        message = "Flawless Quality Standards! Shipment cleared for international ports."
    else:
        final_grade = "Grade B (Local Market)"
        cash_reward = 2500.0
        xp_reward = 50
        message = "Batch downgraded due to manufacturing anomalies."

    # --- Economy Injection Layer ---
    current_user.cash += cash_reward
    current_user.xp += xp_reward

    # Re-calculate level structure using your exact Phase 5 logic format (Every 100 XP increments level)
    # Target XP threshold to clear the current level: (current_user.level * 100)
    level_up_triggered = False
    while current_user.xp >= (current_user.level * 100):
        current_user.level += 1
        level_up_triggered = True

    # --- Secure DB Commits ---
    try:
        db.commit()
        db.refresh(current_user)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Lab engine failed to synchronize transaction ledger with vanguardtex.db"
        )

    return LabAnalysisResponse(
        status="Success",
        batch_id=payload.batch_number,
        fabric_grade=final_grade,
        compliance_report={
            "verdict": message,
            "defects_detected": failed_parameters if failed_parameters else ["None"]
        },
        financials_updated={
            "earned_cash": f"+ Rs. {cash_reward}",
            "earned_xp": f"+ {xp_reward} XP",
            "level_up_event": "YES! 🏆" if level_up_triggered else "NO",
            "current_vault_balance": current_user.cash,
            "current_level": current_user.level
        }
    )
