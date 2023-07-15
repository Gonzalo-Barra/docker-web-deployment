from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Contacto(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: int
    ruc: int

@app.post("/create_contact")
def create_contact(Contacto: Contacto):
    return Contacto

