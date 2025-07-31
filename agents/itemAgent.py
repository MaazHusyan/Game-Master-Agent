import random
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# Sample fantasy items (you can add more)
ITEM_POOL = [
    "Sword of Eternal Flame",
    "Shield of Shadows",
    "Potion of Healing",
    "Ring of Teleportation",
    "Boots of Silent Steps",
    "Scroll of Fireball",
    "Amulet of Truth",
    "Elixir of Strength"
]

def give_item(player_class):
    """
    Selects a random item and describes it using OpenRouter.
    """

    item = random.choice(ITEM_POOL)

    prompt = f"""
You are a fantasy game narrator. The player is a {player_class}.
They have just earned the item: '{item}'.
Describe this item dramatically and tell how it might help the player in future adventures (in 3-4 lines).
"""

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a creative fantasy narrator."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        description = result["choices"][0]["message"]["content"]
        return item, description.strip()
    except Exception as e:
        print(f"Error in ItemAgent: {e}")
        return item, f"You received a {item}, but it seems cursed... 😅"
