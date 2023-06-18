import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        result = "Congratulations! You win!"
    else:
        result = "Sorry! You lose!"

    messagebox.showinfo("Result", result)

def create_gui():
    window = tk.Tk()
    window.title("Rock, Paper, Scissors")

    # Player choices
    rock_button = tk.Button(window, text="Rock", width=10, height=2, command=lambda: play_game("rock"))
    rock_button.grid(row=0, column=0, padx=10, pady=10)
    paper_button = tk.Button(window, text="Paper", width=10, height=2, command=lambda: play_game("paper"))
    paper_button.grid(row=0, column=1, padx=10, pady=10)
    scissors_button = tk.Button(window, text="Scissors", width=10, height=2, command=lambda: play_game("scissors"))
    scissors_button.grid(row=0, column=2, padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
