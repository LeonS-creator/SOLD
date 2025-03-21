from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()

# ✅ Update CORS settings to allow requests from frontend
origins = [
    "https://sold-ten.vercel.app",  # ✅ Corrected Vercel URL
    "https://sold-leons-creators-projects.vercel.app",  # ✅ Corrected Vercel URL
    "http://localhost:3000",  # ✅ Allow localhost for testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ✅ Allow frontend to communicate with the backend
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # ✅ Allow all headers
)

# ✅ Explicitly handle OPTIONS requests (Preflight)
@app.options("/{full_path:path}", include_in_schema=False)
async def options_handler(full_path: str):
    return JSONResponse(content={}, status_code=200)

# Define request model
class UserCreate(BaseModel):
    name: str

# ✅ Registration endpoints
@app.post("/register/user/")
def register_user(user: UserCreate):
    return {"message": f"User {user.name} registered", "qr_code": f"QR_{user.name}"}

@app.post("/register/business/")
def register_business(user: UserCreate):
    return {"message": f"Business {user.name} registered", "qr_code": f"QR_{user.name}"}
