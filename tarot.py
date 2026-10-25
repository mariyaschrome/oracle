import random
import time

cards = {
    "The Fool": "a new beginning and a leap of faith",
    "The Magician": "power, skill, and the will to make it happen",
    "The High Priestess": "secrets, intuition, and what lies beneath",
    "The Empress": "growth, comfort, and creative energy",
    "The Emperor": "control, structure, and strong foundations",
    "The Lovers": "a deep bond and an important choice",
    "The Chariot": "determination and victory through focus",
    "Strength": "quiet courage and gentle power",
    "The Hermit": "solitude and the search for truth",
    "Wheel of Fortune": "luck turning and change on its way",
    "Justice": "truth, fairness, and consequences",
    "The Hanged Man": "pausing, surrender, and a new view",
    "Death": "an ending that clears the way for something new",
    "Temperance": "balance, patience, and healing",
    "The Devil": "temptation, obsession, and chains you can remove",
    "The Tower": "sudden upheaval and truth breaking through",
    "The Star": "hope, renewal, and quiet faith",
    "The Moon": "illusions, dreams, and things not what they seem",
    "The Sun": "joy, success, and clear light",
    "Judgement": "a reckoning and a call to rise",
    "The World": "completion and a chapter beautifully closed",
}

print("🃏 Welcome to the Midnight Tarot 🃏")
input("Focus on your question, then press Enter...")

spread = ["Past", "Present", "Future"]
deck = random.sample(list(cards), 3)

for position, card in zip(spread, deck):
    time.sleep(1.2)
    reversed_card = random.random() < 0.3
    name = card + (" (Reversed)" if reversed_card else "")
    meaning = cards[card]
    if reversed_card: 
        meaning = "the opposite or a block: " + meaning

    print(f"\n✨ {position}: {name}")
    print(f" {meaning.capitalize()}.")

print("\nThe cards have spoken. 🌙")