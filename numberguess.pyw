import tkinter as tk
import random
import sys
import pygame

# Initialize Pygame mixer to play sound
pygame.mixer.init()

# Function to handle the guesses
def check_guess(guess):
    try:
        guess = int(guess)
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    global attempts_left
    if guess > number:
        result_label.config(text=f"Your guess was too high! You have {attempts_left} guesses left.")
    elif guess < number:
        result_label.config(text=f"Your guess was too low! You have {attempts_left} guesses left.")
    else:
        result_label.config(text="Yes, you did it! Good job!")
        return

    attempts_left -= 1
    if attempts_left == 0:
        result_label.config(text=f"Game over! The number was {number}.")
        submit_button.config(state=tk.DISABLED)
    else:
        guess_entry.delete(0, tk.END)

# Function to start a new game
def new_game():
    global number, attempts_left
    number = random.randint(1, 20)
    attempts_left = 3
    result_label.config(text="You have three guesses to guess a random number between 1 and 20!")
    submit_button.config(state=tk.NORMAL)
    guess_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Set fixed window size (not full screen)
root.geometry("400x300")
root.resizable(False, False)  # Disable resizing

# Initialize game variables
number = random.randint(1, 20)
attempts_left = 3

# Title label with slightly smaller font size
title_label = tk.Label(root, text="Number Guessing Game", font=("Arial", 12))
title_label.pack(pady=10)

# Game description label with slightly smaller font size
game_label = tk.Label(root, text="You have three guesses to guess a random number between 1 and 20!", font=("Arial", 9))
game_label.pack(pady=5)

# Entry box for the user to type their guess
guess_entry = tk.Entry(root, font=("Arial", 12))
guess_entry.pack(pady=10)

# Submit button for checking the guess
submit_button = tk.Button(root, text="Submit Guess", font=("Arial", 10), command=lambda: check_guess(guess_entry.get()))
submit_button.pack(pady=10)

# Label to show feedback to the user
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)

# New Game button to restart the game
new_game_button = tk.Button(root, text="Start New Game", font=("Arial", 10), command=new_game)
new_game_button.pack(pady=10)

# Play background music (Ensure you have a music file, e.g., 'background_music.mp3' in the same folder)
pygame.mixer.music.load("gamethemee.mp3")  # Put your music file here
pygame.mixer.music.play(-1, 0.0)  # Loop indefinitely

# Start the main loop
root.mainloop()

# Stop the music when closing the window
pygame.mixer.music.stop()




