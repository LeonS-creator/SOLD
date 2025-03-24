# from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
# from sqlalchemy.orm import relationship
# from app.database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     password_hash = Column(String, nullable=False)
#     qr_code = Column(String, unique=True, nullable=False)

#     businesses = relationship("Business", back_populates="owner")
#     transactions = relationship("Transaction", back_populates="user")

# class Business(Base):
#     __tablename__ = "businesses"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#     category = Column(String)
#     created_at = Column(TIMESTAMP)

#     owner = relationship("User", back_populates="businesses")
#     transactions = relationship("Transaction", back_populates="business")
#     user_points = relationship("UserBusinessPoints", back_populates="business")

# class Transaction(Base):
#     __tablename__ = "transactions"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     business_id = Column(Integer, ForeignKey("businesses.id"))
#     points = Column(Integer, nullable=False)
#     timestamp = Column(TIMESTAMP)

#     user = relationship("User", back_populates="transactions")
#     business = relationship("Business", back_populates="transactions")

# class UserBusinessPoints(Base):
#     __tablename__ = "user_business_points"

#     user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
#     business_id = Column(Integer, ForeignKey("businesses.id"), primary_key=True)
#     total_points = Column(Integer, nullable=False, default=0)

#     user = relationship("User", back_populates="user_points")
#     business = relationship("Business", back_populates="user_points")

# class Coupon(Base):
#     __tablename__ = "coupons"

#     id = Column(Integer, primary_key=True, index=True)
#     business_id = Column(Integer, ForeignKey("businesses.id"))
#     description = Column(String, nullable=False)
#     points_required = Column(Integer, nullable=False)
    
#     business = relationship("Business")


from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    qr_code = Column(String, unique=True, nullable=False)

    businesses = relationship("Business", back_populates="owner")
    transactions = relationship("Transaction", back_populates="user")
    user_business_points = relationship("UserBusinessPoints", back_populates="user")  # 🔥 Korrektur hier!

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String)
    created_at = Column(TIMESTAMP)

    owner = relationship("User", back_populates="businesses")
    transactions = relationship("Transaction", back_populates="business")
    user_business_points = relationship("UserBusinessPoints", back_populates="business")  # 🔥 Korrektur hier!

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    business_id = Column(Integer, ForeignKey("businesses.id"))
    points = Column(Integer, nullable=False)
    timestamp = Column(TIMESTAMP)

    user = relationship("User", back_populates="transactions")
    business = relationship("Business", back_populates="transactions")

class UserBusinessPoints(Base):
    __tablename__ = "user_business_points"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    business_id = Column(Integer, ForeignKey("businesses.id"), primary_key=True)
    total_points = Column(Integer, nullable=False, default=0)

    user = relationship("User", back_populates="user_business_points")  # 🔥 Hier korrigiert
    business = relationship("Business", back_populates="user_business_points")  # 🔥 Hier korrigiert

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))
    description = Column(String, nullable=False)
    points_required = Column(Integer, nullable=False)
    
    business = relationship("Business")
