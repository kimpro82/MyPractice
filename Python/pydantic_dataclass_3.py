"""
Compare Pydantic and @dataclass 3 : @dataclass from pydantic.dataclasses
2024.11.27

It showcases how Pydantic can enforce data types and value constraints
within a dataclass structure.
"""

from typing import List
from pydantic.dataclasses import dataclass
from pydantic import Field

@dataclass
class Superhero:
    name: str
    superpowers: List[str]
    weakness: str
    age: int = Field(..., gt=0, lt=1000)

# Create superheroes
batman = Superhero("Batman", ["Rich", "Smart"], "No superpowers", 35)
superman = Superhero("Superman", ["Flight", "Super strength"], "Kryptonite", 33)

# Print superhero information
print(f"{batman.name}'s superpowers: {', '.join(batman.superpowers)}")
print(f"{superman.name}'s weakness: {superman.weakness}")

# Error case
try:
    weird_hero = Superhero("Weird Guy", ["Sleeping"], "Wife", -5)
    print(f"Weird hero's age: {weird_hero.age}")
except ValueError as e:
    print(f"Error occurred: {e}")
