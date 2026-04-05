import random

def roll_dice():
    return random.randint(1,6)

while True:
    input("Press Enter to roll dice...")
    print("You got:", roll_dice())

    ch = input("Roll again? (y/n): ")
    if ch.lower() != 'y':
        break