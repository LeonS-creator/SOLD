from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base

# Verbindung zu PostgreSQL (ersetze die Werte mit deinen echten Daten)
DATABASE_URL = "postgresql://postgres:SQLLeon@localhost/sold"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
