from agents import Agent

from gemini_model import geminiModel
from _instructions import get_item_agent_instructions


def getItemAgent() -> Agent:
    agent = Agent(
        name="Item Agent",
        instructions= get_item_agent_instructions(),
        tools=[],
        model=geminiModel,
    )

    return agent