import bcrypt
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "VanguardTex_Super_Secret_Key_For_Hackathon_2026"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    # Strings ko bytes mein badal kar standard tarike se hash karna
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        # Check karna ke input password database wale hash se match karta hai ya nahi
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception:
        return False

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
