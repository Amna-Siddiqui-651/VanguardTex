from fastapi import FastAPI
import database

app = FastAPI(title="VanguardTex Backend Engine")

# Jab server start hoga, yeh function database mein real tables bana dega
@app.on_event("startup")
def on_startup():
    database.init_db()
    print("🚀 VanguardTex Database Tables Created Successfully!")

@app.get("/")
def home():
    return {"message": "Welcome to VanguardTex Industrial Simulation Platform!"}
