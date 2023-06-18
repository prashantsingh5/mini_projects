import random
import time

def roll_dice():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice...")
        dice_num = random.randint(1, 6)
        print(f"The dice rolled and you got: {dice_num}")

        roll_again = input("Roll the dice again? (y/n): ")
        if roll_again.lower() != 'y':
            print("Thank you for playing!")
            break

        print()
        time.sleep(1)  # Add a delay for better user experience

roll_dice()
