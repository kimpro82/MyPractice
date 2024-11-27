"""
User Data Handling without Pydantic
2024.11.26

Demonstrates manual implementation of a User class with type checking,
data validation, and JSON serialization. Compares to automated solutions
like Pydantic by showing explicit type conversions and error handling.

Requires Python 3.6+.
"""

import json

class UserManual:
    """
    Represents a user in the system, demonstrating manual implementation
    of type validation and JSON serialization.
    """

    def __init__(self, user_id, name, is_active):
        """
        Initialize a UserManual instance.

        Raises:
            ValueError: If any of the input types are incorrect.
        """
        if not isinstance(user_id, int):
            raise ValueError("id must be an int")
        if not isinstance(name, str):
            raise ValueError("name must be a str")
        if not isinstance(is_active, bool):
            raise ValueError("is_active must be a bool")

        self.user_id = user_id
        self.name = name
        self.is_active = is_active

    def to_json(self):
        """
        Convert the UserManual instance to a JSON string.
        """
        return json.dumps({
            'id': self.user_id,
            'name': self.name,
            'is_active': self.is_active
        })

# Sample user data with string values
user_data_manual = {
    'id': '123',        # Requires explicit conversion to int
    'name': 'Alice',
    'is_active': 'true' # Requires explicit conversion to bool
}

# Manually convert data types and create UserManual instance
user_manual = UserManual(
    int(user_data_manual['id']),
    user_data_manual['name'],
    user_data_manual['is_active'].lower() == 'true'
)

# Serialize to JSON and print
print(user_manual.to_json())
