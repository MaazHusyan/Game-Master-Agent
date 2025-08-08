from agents import Agent

from my_tools.roll_dice import rollDice
from gemini_model import geminiModel
from _instructions import get_monster_agent_instructions


def getMonsterAgent() -> Agent:
    agent = Agent(
        name= "Monster Agent",
        instructions= get_monster_agent_instructions(),
        tools= [rollDice],
        model= geminiModel
    )
    
    return agent