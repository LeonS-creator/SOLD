from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ Allow requests from your frontend on Vercel
origins = [
    "sold-ten.vercel.app",  # Replace with your actual Vercel URL
    "sold-leons-creators-projects.vercel.app",
    "http://localhost:3000",  # Allow localhost for testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow frontend to communicate with the backend
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # ✅ Allow all headers
)

class UserCreate(BaseModel):
    name: str

@app.post("/register/user/")
def register_user(user: UserCreate):
    return {"message": f"User {user.name} registered", "qr_code": f"QR_{user.name}"}

@app.post("/register/business/")
def register_business(user: UserCreate):
    return {"message": f"Business {user.name} registered", "qr_code": f"QR_{user.name}"}
