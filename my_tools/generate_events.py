import random

from agents import function_tool


@function_tool
def generateEvents():
    """Generates a random event for the game."""
    print("The event generation tool is now active.")
    events = [
        "You find a hidden treasure chest filled with gold!",
        "A wild beast appears and challenges you to a fight.",
        "You stumble upon an ancient ruin with mysterious artifacts.",
        "A friendly villager offers you a quest to help them.",
        "You discover a magical portal that leads to another realm."
    ]
    return random.choice(events)