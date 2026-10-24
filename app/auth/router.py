from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.models import User
from app.auth.schemas import UserCreate, UserLogin, Token
from app.auth.utils import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Industrial Access Management (Auth)"]
)

# Route 1: Naya worker ya admin register karne ke liye
@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    # Check karein agar username ya email pehle se exist karta ho
    db_user = db.query(User).filter((User.username == user_data.username) | (User.email == user_data.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or Email already registered")
    
    # Secure encrypted password ke sath user save karein
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    return {"message": f"User {new_user.username} successfully registered as {new_user.role}!"}

# Route 2: Secure JWT Token generate karne ke liye
@router.post("/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == login_data.username).first()
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Token ke andar payload data chupa rahe hain
    token_data = {"user_id": user.id, "role": user.role, "username": user.username}
    token = create_access_token(data=token_data)
    
    return {"access_token": token, "token_type": "bearer"}
