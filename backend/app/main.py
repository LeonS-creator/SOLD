from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ Allow CORS for frontend on localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all methods (GET, POST, etc.)
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
