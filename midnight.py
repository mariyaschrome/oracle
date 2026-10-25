import random
import time
from datetime import date 

answers = {
    "yes": ["The stars lean toward yes.", "Yes. The shadows have already agreed."],
    "no": ["The candle flickers. No.", "The raven shakes its head. No."],
    "maybe": ["The cards are tangled. Ask again at midnight,", "The future is still deciding."],
}

cards = {
    "The Fool": "a new beginning and a leap of faith",
    "The Magician": "power, skill, and the will to make it happen",
    "The High Priestess": "secrets, intuition, and what lies beneath",
    "The Lovers": "a deep bond and an important choice",
    "The Tower": "sudden upheaval and truth breaking through",
    "The Star": "hope, renewal, and quiet faith",
    "The Moon": "illusions, dreams, and things not what they seem",
    "The Sun": "joy, success, and clear light",
}


def dramatic(text):
    print(f"\n🕯️ {text}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.7)
        print(".", end="", flush=True)
    print()

def ask_oracle():
    question = input("\nYour question: ").strip()
    if not question:
        print("The Oracle cannot answer silence.")
        return
    dramatic("The Oracle gazes into the mist")
    kind = random.choice(list(answers))
    print("✨", random.choice(answers[kind]))

def tarot():
    input("\nFocus on your question, the press Enter...")
    labels = ["Past", "Present", "Future"]
    for label, card in zip(labels, random.sample(list(cards), 3)):
        time.sleep(1.2)
        flipped = random.random() < 0.3
        meaning = ("the opposite or a block: " if flipped else "") + cards[card]
        print(f"\n✨ {label}: {card}{' (Reversed)' if flipped else ''}")
        print(f" {meaning.capitalize()}.")

def card_of_the_day():
    rng = random.Random(str(date.today()))
    card = rng.choice(list(cards))
    dramatic("Turning today's card")
    print(f"✨ {card}: {cards[card].capitalize()}.")

menu = {
    "1": ("Ask the Oracle", ask_oracle),
    "2": ("Three-card tarot reading", tarot),
    "3": ("Card of the day", card_of_the_day),
}

print("🔮 Welcome to the Midnight Bot 🔮")

while True:
    print("\n" + "-" * 30)
    for key, (label, _) in menu.items():
        print(f"{key}. {label}")
    print("q. Leave")

    choice = input("\nChoose: ").strip().lower()

    if choice == "q":
        print("The dark welcomes you back anytime. 🌙")
        break
    elif choice in menu:
        menu[choice][1]()
    else:
        print("The Oracle does not understand that choice.")