import random
import time

def play_game():
    print("Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")

    level = select_level()
    secret_number = generate_secret_number(level)

    attempts = 0
    start_time = time.time()

    while True:
        guess = take_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            score = calculate_score(level, attempts, elapsed_time)

            print(f"\nCongratulations {name}! You guessed the number in {attempts} attempts.")
            print(f"Your time: {elapsed_time} seconds")
            print(f"Score: {score}")

            save_score(name, level, score)
            break

def select_level():
    print("\nSelect the difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please try again.")

def generate_secret_number(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 50)
    elif level == 3:
        return random.randint(1, 100)

def take_guess():
    while True:
        try:
            guess = int(input("\nTake a guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_score(level, attempts, elapsed_time):
    level_multipliers = {1: 10, 2: 5, 3: 2}
    score = level_multipliers[level] * (100 - attempts) / elapsed_time
    return round(score, 2)

def save_score(name, level, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name} - Level: {level} - Score: {score}\n")

def show_scores():
    print("\n--- High Scores ---")
    with open("scores.txt", "r") as file:
        scores = file.read()
        if scores:
            print(scores)
        else:
            print("No scores found.")

def main():
    print("==== Number Guessing Game ====")
    while True:
        print("\n1. Play Game")
        print("2. Show High Scores")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            play_game()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
