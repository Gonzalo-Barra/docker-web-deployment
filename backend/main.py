from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://admin:root@localhost:5432/Contactos"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Contacto(Base):
    __tablename__="contactos"
    id = Column(Integer(), primary_key=True)
    nombre = Column(String, index=True)
    apellido = Column(String, nullable=False)
    email = Column(String())
    telefono = Column(BigInteger())
    ruc = Column(BigInteger())

Base.metadata.create_all(bind=engine)
####
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Contacto(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: int
    ruc: int

@app.post("/create_contact")
def create_contact(Contacto: Contacto):
    return Contacto

