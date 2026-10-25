from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import jwt

from app.database import get_db
from app.auth.models import User
from app.auth.schemas import UserCreate, Token
from app.auth.utils import hash_password, verify_password, create_access_token, SECRET_KEY, ALGORITHM

router = APIRouter(
    prefix="/auth",
    tags=["Industrial Access Management (Auth)"]
)

# Route 1: Worker ya Admin register karne ke liye
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


# Route 2: Direct Swagger Login Support! 🔥
@router.post("/login", response_model=Token)
def login(login_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == login_data.username).first()
    
    # Standard security password validation checking database hashed value
    if not user or not verify_password(login_data.password, user.hashed_password): 
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Token payload definition
    token_data = {"user_id": user.id, "role": user.role, "username": user.username}
    token = create_access_token(data=token_data)
    
    return {"access_token": token, "token_type": "bearer"}


# --- SECURITY LOCK ENGINE AREA ---
# Token link set for automatic swagger documentation popup locking
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login") 

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Token decode implementation
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
        
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user
