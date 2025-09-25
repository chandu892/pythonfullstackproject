# src/logic.py

from typing import Dict, Any


class Pet:
    def __init__(self, name: str, pet_type: str,
                 hunger: int = 50, happiness: int = 50,
                 energy: int = 50, cleanliness: int = 50,
                 age: int = 0, pet_id: int = None):
        self.pet_id = pet_id
        self.name = name
        self.type = pet_type
        self.hunger = max(0, min(100, int(hunger)))
        self.happiness = max(0, min(100, int(happiness)))
        self.energy = max(0, min(100, int(energy)))
        self.cleanliness = max(0, min(100, int(cleanliness)))
        self.age = int(age)

    def feed(self) -> str:
        self.hunger = min(100, self.hunger + 20)
        self.energy = min(100, self.energy + 10)
        return f"{self.name} has been fed. Hunger: {self.hunger}"

    def play(self) -> str:
        if self.energy < 10:
            return f"{self.name} is too tired to play."
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        self.hunger = max(0, self.hunger - 5)
        return f"{self.name} played and is happier! Happiness: {self.happiness}"

    def clean(self) -> str:
        self.cleanliness = 100
        return f"{self.name} is clean now."

    def decay(self):
        """Simulate time passing"""
        self.hunger = max(0, self.hunger - 5)
        self.happiness = max(0, self.happiness - 2)
        self.energy = max(0, self.energy - 3)
        self.cleanliness = max(0, self.cleanliness - 1)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pet_id": self.pet_id,
            "name": self.name,
            "type": self.type,
            "hunger": self.hunger,
            "happiness": self.happiness,
            "energy": self.energy,
            "cleanliness": self.cleanliness,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pet":
        return cls(
            name=data.get("name"),
            pet_type=data.get("type"),
            hunger=data.get("hunger", 50),
            happiness=data.get("happiness", 50),
            energy=data.get("energy", 50),
            cleanliness=data.get("cleanliness", 50),
            age=data.get("age", 0),
            pet_id=data.get("pet_id")
        )
