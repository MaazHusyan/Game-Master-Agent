from agents import Agent

from my_tools.generate_events import generateEvents
from gemini_model import geminiModel
from _instructions import get_narrator_agent_instructions

print("Narrator Agent Activated")
def getNarratorAgent()-> Agent:
    agent = Agent(
        name= "Narrator Agent",
        instructions= get_narrator_agent_instructions(),
        tools= [generateEvents],
        model= geminiModel
    )
    
    return agent