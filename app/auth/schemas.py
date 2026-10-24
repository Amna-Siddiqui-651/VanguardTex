from pydantic import BaseModel, EmailStr
from typing import Optional

# Signup karte waqt user se kya data lena hai
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = "Worker"  # Defaut role Worker hoga, Admin bhi ho sakta hai

# Login karte waqt user se kya data lena hai
class UserLogin(BaseModel):
    username: str
    password: str

# Login ke baad response mein token dene ke liye
class Token(BaseModel):
    access_token: str
    token_type: str
