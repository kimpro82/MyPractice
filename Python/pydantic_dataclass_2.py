"""
Comparing Pydantic and @dataclass 2 : Pydantic BaseModel instead of @dataclass
2024.11.27

It showcases how Pydantic can enforce data types and value constraints.
"""

from typing import List
from pydantic import BaseModel, Field

class Superhero(BaseModel):
    name: str
    superpowers: List[str]
    weakness: str
    age: int = Field(..., gt=0, lt=1000)

# Create superheroes
batman = Superhero(name="Batman", superpowers=["Rich", "Smart"], weakness="No superpowers", age=35)
superman = Superhero(name="Superman", superpowers=["Flight", "Super strength"], weakness="Kryptonite", age=33)

# Print superhero information
print(f"{batman.name}'s superpowers: {', '.join(batman.superpowers)}")
print(f"{superman.name}'s weakness: {superman.weakness}")

# Error case
try:
    weird_hero = Superhero(name="Weird Guy", superpowers=["Sleeping"], weakness="Wife", age=-5)
    print(f"Weird hero's age: {weird_hero.age}")
except ValueError as e:
    print(f"Error occurred: {e}")
