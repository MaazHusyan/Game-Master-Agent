import random

from agents import function_tool    


@function_tool
def rollDice(sides=6):
    """Rolls a dice with a specified number of sides."""
    result = random.randint(1, sides)
    print(f"Result: {result}")
    return result