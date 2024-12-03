"""
Abstract Base Class(ABC) as Interface Practice
2024.11.30

It showcases how abstract methods can be used to define a common interface
for different types of mischievous actions.
"""

from abc import ABC, abstractmethod

class MischievousBoy(ABC):
    """Abstract base class defining the interface for mischievous boys."""
    @abstractmethod
    def play_prank(self):
        """Play a prank on someone."""
        # pass  # not necessary

    @abstractmethod
    def get_in_trouble(self):
        """Get into trouble for doing something naughty."""
        # pass  # not necessary

class Timmy(MischievousBoy):
    """Concrete class representing Timmy, a mischievous boy."""
    def play_prank(self):
        """Timmy's specific implementation of playing a prank."""
        print("Timmy puts a whoopee cushion on the teacher's chair!")

    def get_in_trouble(self):
        """Timmy's specific way of getting into trouble."""
        print("Timmy gets detention for drawing on the walls.")

class Johnny(MischievousBoy):
    """Concrete class representing Johnny, another mischievous boy."""
    def play_prank(self):
        """Johnny's specific implementation of playing a prank."""
        print("Johnny hides all the chalk in the classroom!")

    def get_in_trouble(self):
        """Johnny's specific way of getting into trouble."""
        print("Johnny has to clean the blackboard for a week.")

# Create instances of the mischievous boys
timmy = Timmy()
johnny = Johnny()

# Demonstrate Timmy and Johnny in action
timmy.play_prank()
timmy.get_in_trouble()

johnny.play_prank()
johnny.get_in_trouble()
