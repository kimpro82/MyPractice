"""
User Data Handling with Pydantic
2024.11.26

Demonstrates Pydantic's capabilities for data validation and serialization.
Defines a User model, creates an instance from a dictionary with automatic
type conversion, and serializes to JSON.

Requires Python 3.7+ and Pydantic library.
"""

from pydantic import BaseModel

class User(BaseModel):
    """
    Represents a user in the system.
    """
    id: int
    name: str
    is_active: bool

# Sample user data with string values
user_data = {
    'id': '123',        # Will be automatically converted to int
    'name': 'Alice',
    'is_active': 'true' # Will be automatically converted to bool
}

# Create a User instance from the dictionary
# Pydantic will automatically validate and convert the data types
user = User(**user_data)

# Print the user object as a JSON string
print(user.model_dump_json())
