"""
Comparing Pydantic and @dataclass 1 : @dataclass without Pydantic
2024.11.27

It showcases basic functionality without data validation.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Superhero:
    name: str
    superpowers: List[str]
    weakness: str
    age: int

# Create superheroes
batman = Superhero("Batman", ["Rich", "Smart"], "No superpowers", 35)
superman = Superhero("Superman", ["Flight", "Super strength"], "Kryptonite", 33)

# Print superhero information
print(f"{batman.name}'s superpowers: {', '.join(batman.superpowers)}")
print(f"{superman.name}'s weakness: {superman.weakness}")

# This case doesn't raise an error but is logically incorrect
weird_hero = Superhero("Weird Guy", ["Sleeping"], "Wife", -5)
print(f"Weird hero's age: {weird_hero.age}")  # Negative age is allowed
