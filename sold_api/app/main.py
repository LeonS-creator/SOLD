from fastapi import FastAPI
from app import models, database
from app.routes import router

app = FastAPI()

# API-Routen einbinden
app.include_router(router)

# Datenbank-Tabellen erstellen
models.Base.metadata.create_all(bind=database.engine)

# from fastapi import FastAPI
# from app.routes import router

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "SOLD API is running!"}

# API-Routen einbinden
# app.include_router(router)
