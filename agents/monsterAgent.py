import random
import requests
import os
from dotenv import load_dotenv
from tools.game_tools import roll_dice

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def handle_combat(player_class, monster_name):
    """
    Simulates a combat encounter and narrates the result.
    """

    player_roll = roll_dice()
    monster_roll = roll_dice()

    print(f"🌀 You rolled a {player_roll}")
    print(f"👹 Monster rolled a {monster_roll}")

    outcome = "draw"
    if player_roll > monster_roll:
        outcome = "win"
    elif player_roll < monster_roll:
        outcome = "lose"

    prompt = f"""
You are a fantasy battle narrator. A {player_class} is fighting a {monster_name}.
The player rolled {player_roll}, and the monster rolled {monster_roll}.
The outcome is: {outcome}.
Narrate the result dramatically in 2-4 lines.
"""

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a dramatic fantasy battle narrator."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        narration = result["choices"][0]["message"]["content"]
        return outcome.capitalize(), narration.strip()
    except Exception as e:
        print(f"Error in MonsterAgent: {e}")
        return "Draw", "A wild blur of chaos ensues, but no clear outcome is seen..."
