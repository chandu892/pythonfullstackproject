# db_manager.py
import os
import json
from supabase import create_client
from dotenv import load_dotenv

# Load Environment Variables 
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Supabase CRUD 
def create_pet(name, pet_type, hunger=50, happiness=50, energy=50, cleanliness=50, age=0, created_at=None):
    """Insert a new pet record into Supabase."""
    data = {
        "name": name,
        "type": pet_type,
        "hunger": hunger,
        "happiness": happiness,
        "energy": energy,
        "cleanliness": cleanliness,
        "age": age,
    }
    if created_at:
        data["created_at"] = created_at

    response = supabase.table("pets").insert(data).execute()
    return response.data


def get_pets():
    """Fetch all pets from Supabase."""
    response = supabase.table("pets").select("*").execute()
    return response.data


def update_pet(pet_id, updates: dict):
    """Update a pet record by ID."""
    response = supabase.table("pets").update(updates).eq("pet_id", pet_id).execute()
    return response.data


def delete_pet(pet_id):
    """Delete a pet record by ID."""
    response = supabase.table("pets").delete().eq("pet_id", pet_id).execute()
    return response.data


DB_FILE = "pets.json"

def load_pets():
    """Load pets from local JSON file."""
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_pets(pets):
    """Save pets to local JSON file."""
    with open(DB_FILE, "w") as f:
        json.dump(pets, f, indent=4)

def update_pet_local(pet_index, updates: dict):
    """Update a pet in local JSON by index."""
    pets = load_pets()
    if 0 <= pet_index < len(pets):
        pets[pet_index].update(updates)
        save_pets(pets)
        return pets[pet_index]
    return None

def delete_pet_local(pet_index):
    """Delete a pet from local JSON by index."""
    pets = load_pets()
    if 0 <= pet_index < len(pets):
        removed = pets.pop(pet_index)
        save_pets(pets)
        return removed
    return None
