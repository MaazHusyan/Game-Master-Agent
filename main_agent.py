import asyncio

from agents import(
    Agent,
    Runner,
    SQLiteSession
)

from _instructions import get_game_master_instructions

from my_sgents.item_agent import getItemAgent
from my_sgents.monster_agent import getMonsterAgent
from my_sgents.narrator_agent import getNarratorAgent

from my_tools.generate_events import generateEvents
from my_tools.roll_dice import rollDice

from gemini_model import geminiModel, config

def mainAgent()-> Agent:
    agent = Agent(
        name= "game Master Agent",
        instructions= get_game_master_instructions(),
        tools= [generateEvents, rollDice],
        handoffs= [
            getItemAgent(),
            getMonsterAgent(),
            getNarratorAgent()
        ],
        model= geminiModel
    )
    
    return agent


async def runMainAgent():
    agent = mainAgent()
    session = SQLiteSession("user_Maaz", "chat_history.db")
    
    print("WELLCOME TO GAME MASTER AGENT")
    while True:
        playerInput = input("🧑🏽: ").strip()
        
        if playerInput.lower() in ["stop", "quit", "exit"]:
            print("Exiting Game master. Goodbye!")
            break
        
        result = await Runner.run(
            starting_agent= agent,
            input= playerInput,
            run_config= config,
            session= session,
            max_turns= 15
        )
        
        print(f"🤖: {result.final_output}")
        
if __name__ == "__main__":
    asyncio.run(runMainAgent())