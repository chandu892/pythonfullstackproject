# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List

import os
import sys
# make sure src is importable when running from api folder
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from src import db  # import our db wrapper
from src.logic import Pet

app = FastAPI(title="Virtual Pet API")

# enable CORS so streamlit or other frontends can call it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for production tighten this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PetCreate(BaseModel):
    name: str = Field(..., example="Buddy")
    type: str = Field(..., example="dog")
    hunger: Optional[int] = 50
    happiness: Optional[int] = 50
    energy: Optional[int] = 50
    cleanliness: Optional[int] = 50
    age: Optional[int] = 0


class PetUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]
    hunger: Optional[int]
    happiness: Optional[int]
    energy: Optional[int]
    cleanliness: Optional[int]
    age: Optional[int]


class PetOut(PetCreate):
    pet_id: Optional[int]


@app.post("/pets/", response_model=PetOut)
def api_create_pet(payload: PetCreate):
    rec = db.create_pet(
        name=payload.name,
        pet_type=payload.type,
        hunger=payload.hunger,
        happiness=payload.happiness,
        energy=payload.energy,
        cleanliness=payload.cleanliness,
        age=payload.age
    )
    return rec


@app.get("/pets/", response_model=List[PetOut])
def api_list_pets():
    recs = db.get_pets()
    return recs


@app.get("/pets/{pet_id}", response_model=PetOut)
def api_get_pet(pet_id: int):
    rec = db.get_pet(pet_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Pet not found")
    return rec


@app.put("/pets/{pet_id}", response_model=PetOut)
def api_update_pet(pet_id: int, payload: PetUpdate):
    updates = {k: v for k, v in payload.dict().items() if v is not None}
    if not updates:
        raise HTTPException(status_code=400, detail="No updates provided")
    rec = db.update_pet(pet_id, updates)
    if not rec:
        raise HTTPException(status_code=404, detail="Pet not found")
    return rec


@app.delete("/pets/{pet_id}", response_model=PetOut)
def api_delete_pet(pet_id: int):
    rec = db.delete_pet(pet_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Pet not found")
    return rec
