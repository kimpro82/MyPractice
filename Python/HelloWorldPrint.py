"""
hello_world("print")
2024.05.23

Example usage:
hello_world("print")

Output:
hello_world
"""

import sys

def hello_world(func_name):
    """
    Dynamically call the given function using its name.
    The name of the current executing function is passed as an argument.

    Caution:
        Using eval() can pose security risks!

    Args:
        func_name (str): Name of the function to be called

    Returns:
        None
    """
    current_func_name = sys._getframe().f_code.co_name
    func = eval(func_name)
    func(current_func_name)

if __name__ == "__main__":
    hello_world("print")
