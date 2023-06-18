import time
import random

def calculate_typing_speed(start_time, end_time, text):
    total_time = end_time - start_time
    words = len(text.split())
    speed = (words / total_time) * 60
    return speed

def generate_random_text():
    words = ["Lorem", "ipsum", "dolor", "sit", "amet,", "consectetur",
             "adipiscing", "elit,", "sed", "do", "eiusmod", "tempor",
             "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua."]
    random.shuffle(words)
    return " ".join(words)

def main():
    print("Welcome to the Speed Typing Test!")

    # Generate random text for typing test
    text = generate_random_text()

    # Prompt the user to start the test
    input("Press Enter to start the test...")

    # Get the current time as the start time
    start_time = time.time()

    # Prompt the user to type the given text
    user_input = input(text + "\n")

    # Get the current time as the end time
    end_time = time.time()

    # Calculate the typing speed
    speed = calculate_typing_speed(start_time, end_time, text)

    # Calculate accuracy
    correct_characters = sum([1 for i, c in enumerate(user_input) if c == text[i]])
    accuracy = (correct_characters / len(text)) * 100

    # Print the result
    print("Typing speed:", round(speed, 2), "words per minute")
    print("Accuracy:", round(accuracy, 2), "%")

if __name__ == '__main__':
    main()
