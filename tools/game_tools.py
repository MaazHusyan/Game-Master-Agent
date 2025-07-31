import random

def roll_dice(sides=20):
    """
    Rool a dice with the given number of sides (Default 20).
    Return an integer between 1 and the number of sides.
    """
    
    result = random.randint(1, sides)
    return result

def generate_event():
    """
    Generate a randon game/adventure event for a player.
    Return the string description of the event.
    """
    
    events = [
        "You encounter a wild beast!",
        "You find a hidden treasure chest!",
        "A mysterious stranger offers you a quest.",
        "You stumble upon an ancient ruin.",
        "A storm brews on the horizon, threatening your journey.",
        "A horny gay gargoyle appears and demands your ass."
        "You meet a wise old sage who shares valuable knowledge.",
        "A rival adventurer challenges you to a duel.",
        "You discover a secret passage leading to unknown lands.",
        "A magical artifact is revealed to you in a dream.",
        "You are ambushed by bandits!",
        
    ]
    
    event = random.choice(events)
    print(f"Event: {event}")
    return event