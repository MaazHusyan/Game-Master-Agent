from agents.narratorAgent import get_narration
from agents.monsterAgent import handle_combat
from agents.itemAgent import give_item
from tools.game_tools import roll_dice, generate_event

def main():
    print("🎮 Welcome to the Fantasy Adventure Game!")
    name = input("🧙 What's your character's name? > ")
    char_class = input("⚔️ Choose your class (warrior, mage, rogue, etc.): > ")

    print("\n📜 Let the adventure begin...\n")

    print(get_narration(name, char_class))

    while True:
        choice = input("\n👉 What will you do next? (explore/fight/item/quit): > ").strip().lower()

        if choice == "explore":
            event = generate_event()
            print(f"\n🌲 Event: {event}")
            story = get_narration(name, char_class, event)
            print(story)

        elif choice == "fight":
            outcome, story = handle_combat(name, char_class)
            print(f"\n👾 Monster Fight Result: {outcome}")
            print(story)

        elif choice == "item":
            item, desc = give_item(char_class)
            print(f"\n🎁 Item Acquired: {item}")
            print(desc)

        elif choice == "quit":
            print("\n👋 Thanks for playing! May your legend live on.")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
