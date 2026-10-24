from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# 1. Database Connection Link (Yeh auto local file 'vanguardtex.db' bana dega)
DATABASE_URL = "sqlite:///./vanguardtex.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 2. DATABASE MODELS (Python Classes jo automatic Tables banengi)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    cash = Column(Integer, default=10000)  # Starting budget for player

    # Inventory table ke sath relationship link
    inventory = relationship("Inventory", back_populates="owner", uselist=False)


class Inventory(Base):
    __tablename__ = "inventories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    cotton_kg = Column(Integer, default=100)       # Starting raw material
    polyester_kg = Column(Integer, default=50)     # Starting raw material
    dye_liters = Column(Integer, default=20)       # Starting chemicals

    owner = relationship("User", back_populates="inventory")

# 3. Tables ko real-time database mein initialize karne ka function
def init_db():
    Base.metadata.create_all(bind=engine)
