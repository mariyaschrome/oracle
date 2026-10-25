import random
import time

answers = {
    "yes": [
        "The stars lean toward yes.",
        "Yes. The shadows have already agreed.",
        "Without a doubt. The moon is on your side.",
        "It is written. Yes."
    ],
    "no": [
        "The candle flickers. No.",
        "Not this time. The omens are dark.",
        "The raven shakes its head. No.",
        "The mist says no.",
    ], 
    "maybe": [
        "The cards are tangled. Ask again at midnight.",
        "The answer is hidden. Look within.",
        "Maybe. But it will cost you something.",
        "The future is still deciding.",
    ],
}

print("🔮 Welcome to the Midnight Oracle 🔮")
print("Ask me anything. Type 'quit' to leave.\n")

while True:
    question = input("Your question: ")

    if question.lower() == "quit":
        print("The Oracle cannot answer silence.\n")
        continue

    print("\n🕯️  The Oracle gazes into the mist", end="", flush=True)
    for _ in range(3):
        time.sleep(0.7)
        print(".", end="", flush=True)

    kind = random.choice(list(answers))
    print("\n✨", random.choice(answers[kind]), "\n")