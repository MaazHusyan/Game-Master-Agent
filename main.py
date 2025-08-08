import asyncio

from agents import(
    Agent,
    Runner,
    SQLiteSession
)

from _instructions import get_game_master_instructions
from my_sgents import(
    item_agent,
    monster_agent,
    narrator_agent
)
from my_tools import(
    generate_events,
    roll_dice 
)
from gemini_model import geminiModel, config

def mainAgent()-> Agent:
    agent = Agent(
        name= "game Master Agent",
        instructions= get_game_master_instructions(),
        tools= [generate_events, roll_dice],
        handoffs= [
            item_agent,
            monster_agent,
            narrator_agent
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
            max_turns= 5
        )
        
        print(f"🤖: {result.final_output}")
        
if __name__ == "__main__":
    asyncio.run(runMainAgent())