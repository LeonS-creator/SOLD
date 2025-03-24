from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from pydantic import BaseModel
from passlib.context import CryptContext
import uuid

router = APIRouter()

# 🆕 Pydantic-Modell für User-Registrierung
class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str

# Passwort-Verschlüsselung (für später, aktuell unverschlüsselt vergleichen)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔹 0️⃣ Nutzer erstellen
# @router.post("/users/")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     # Optional: check if user already exists
#     existing_user = db.query(models.User).filter(models.User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")

#     new_user = models.User(
#         name=user.name,
#         email=user.email,
#         password_hash=user.password,  # ⛔ Später durch Hash ersetzen
#         qr_code="TODO"
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message": "User created", "user_id": new_user.id}

# @router.post("/users/")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(models.User).filter(models.User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")

#     # 🛡️ Passwort hashen
#     hashed_password = pwd_context.hash(user.password)

#     new_user = models.User(
#         name=user.name,
#         email=user.email,
#         password_hash=hashed_password,
#         qr_code="TODO"
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message": "User created", "user_id": new_user.id}

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(user.password)

    # Erzeuge eindeutigen QR-Code als UUID (z.B. später ersetzt durch echte Logik)
    qr_code = str(uuid.uuid4())

    new_user = models.User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password,
        qr_code=qr_code
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created", "user_id": new_user.id, "qr_code": qr_code}


# 🔹 1️⃣ Nutzer abrufen
@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 🔹 2️⃣ Geschäft abrufen
@router.get("/businesses/{business_id}")
def get_business(business_id: int, db: Session = Depends(get_db)):
    business = db.query(models.Business).filter(models.Business.id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business

# 🔹 3️⃣ Punkte eines Nutzers in einem Geschäft abrufen
@router.get("/users/{user_id}/points")
def get_user_points(user_id: int, db: Session = Depends(get_db)):
    user_points = db.query(models.UserBusinessPoints).filter(models.UserBusinessPoints.user_id == user_id).all()
    return user_points

# 🔹 4️⃣ Punkte-Transaktion hinzufügen
@router.post("/transactions/")
def add_transaction(user_id: int, business_id: int, points: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    business = db.query(models.Business).filter(models.Business.id == business_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")

    new_transaction = models.Transaction(user_id=user_id, business_id=business_id, points=points)
    db.add(new_transaction)

    user_points_entry = db.query(models.UserBusinessPoints).filter(
        models.UserBusinessPoints.user_id == user_id,
        models.UserBusinessPoints.business_id == business_id
    ).first()

    if user_points_entry:
        user_points_entry.total_points += points
    else:
        user_points_entry = models.UserBusinessPoints(
            user_id=user_id,
            business_id=business_id,
            total_points=points
        )
        db.add(user_points_entry)

    db.commit()
    return {"message": "Transaction added", "user_id": user_id, "business_id": business_id, "points": points}

# 🔹 5️⃣ Verfügbare Coupons für ein Geschäft abrufen
@router.get("/businesses/{business_id}/coupons")
def get_coupons(business_id: int, db: Session = Depends(get_db)):
    coupons = db.query(models.Coupon).filter(models.Coupon.business_id == business_id).all()
    return coupons

# 🔹 6️⃣ Coupon einlösen
@router.post("/users/{user_id}/redeem_coupon/")
def redeem_coupon(user_id: int, coupon_id: int, db: Session = Depends(get_db)):
    coupon = db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()
    user_points = db.query(models.UserBusinessPoints).filter(
        models.UserBusinessPoints.user_id == user_id,
        models.UserBusinessPoints.business_id == coupon.business_id
    ).first()

    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")
    
    if not user_points or user_points.total_points < coupon.points_required:
        raise HTTPException(status_code=400, detail="Not enough points")

    user_points.total_points -= coupon.points_required
    db.commit()

    return {"message": "Coupon redeemed", "user_id": user_id, "coupon_id": coupon_id}


# @router.post("/login/")
# def login_user(email: str, password: str, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == email).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Aktuell: Passwort noch unverschlüsselt gespeichert
#     if user.password_hash != password:
#         raise HTTPException(status_code=401, detail="Incorrect password")

#     # Erfolgreich eingeloggt → gib Nutzer-ID zurück
#     return {"message": "Login successful", "user_id": user.id}

# @router.post("/login/")
# def login_user(email: str, password: str, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == email).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # ✅ Hashed Passwort prüfen
#     if not pwd_context.verify(password, user.password_hash):
#         raise HTTPException(status_code=401, detail="Incorrect password")

#     return {"message": "Login successful", "user_id": user.id}

@router.post("/login/")
def login_user(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == login_data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not pwd_context.verify(login_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {"message": "Login successful", "user_id": user.id}

