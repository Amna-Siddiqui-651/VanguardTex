from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="Worker")  # Roles: "Admin" ya "Worker"

 # --- Economy & Gamification Stats 🔥 ---
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    cash = Column(Integer, default=10000)  # Shuru mein har player ko 10,000 PKR milenge!