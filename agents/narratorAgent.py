import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def get_narration(player_name, player_class, player_action=None):
    """
    Returns the next part of the story based on player class and action.
    If no action is provided, generate the intro.
    """
    if not player_action:
        return (
            f"In the realm of Eldoria, where magic and steel clash in an eternal dance, "
            f"a {player_name} of valiant heart emerges. With his powerful stance and the shimmer of his enchanted armor, "
            f"the {player_class} stands tall, ready to face the onslaught of the dark forces besieging his land. "
            "The cry of his war horn echoes through the valley, a call to arms for the beleaguered townsfolk, "
            "a beacon of hope in the dark hour. The fate of Eldoria balances upon the edge of his sword."
        )

    # Otherwise, generate a dynamic story based on the action
    prompt = f"""
You are a fantasy story narrator in a text-based game.

The player is a {player_class}. Based on the following action, continue the story:

Player action: {player_action}

Respond with a 2-4 line narration only.
"""

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful, dramatic fantasy narrator."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        narration = result["choices"][0]["message"]["content"]
        return narration.strip()
    except Exception as e:
        print(f"❌ Error in NarratorAgent: {e}")
        return "The winds whisper, but no story unfolds..."
