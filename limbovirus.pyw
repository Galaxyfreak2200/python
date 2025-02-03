import tkinter as tk
import math
import random
import pygame  # Import pygame for music

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("1090101_Nighthawk22---Isolation-Of.mp3")  # Replace with your actual file name
pygame.mixer.music.play(-1)  # Loop the music indefinitely

root = tk.Tk()
root.config(bg="black")
root.title("Limbo Virus Ver 1.0")

# Set the window to full screen
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))  # Press Esc to exit fullscreen

# Get screen size for dynamic centering
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Oval shape parameters
center_x, center_y = screen_width / 2, screen_height / 2  # Center of the screen
a, b = 150, 70  # Horizontal and vertical radii
num_keys = 8  # Number of keys
angle_step = 2 * math.pi / num_keys  # Angle step for each key
speed = 50  # Speed of rotation (lower = faster)
key_size = 30  # Estimated size of emoji in pixels

# Colors for the keys in specified order
colors = ["red", "green", "yellow", "blue", "purple", "lime", "pink", "teal"]

# Create key labels
labels = []
angles = [i * angle_step for i in range(num_keys)]  # Initial angles

# Function when key is clicked or space bar is pressed
def key_clicked(event=None):
    if random.randint(1, 8) == 1:  # 1 in 8 chance
        result_label.config(text="Success!", fg="lime")
        root.after(1000, root.quit)  # Close the program after 1 second
    else:
        result_label.config(text="Try Again!", fg="red")

# Create keys and assign click event
for i in range(num_keys):
    label = tk.Label(root, text="🗝️", bg="black", fg=colors[i], font=("Arial", 20), cursor="hand2")
    label.place(x=0, y=0)
    label.bind("<Button-1>", lambda event: key_clicked())  # Bind left-click event to the key
    labels.append(label)

# Display result text
result_label = tk.Label(root, text="", bg="black", fg="white", font=("Arial", 16))
result_label.place(x=screen_width / 2 - 80, y=screen_height - 50)

# Bind space bar to the key_clicked function
root.bind("<space>", key_clicked)

# Function to update positions (centered correctly)
def update_positions():
    global angles
    for i in range(num_keys):
        angles[i] += 0.1  # Rotate each key slightly (adjust for speed)
        x = center_x + a * math.cos(angles[i]) - key_size / 2
        y = center_y + b * math.sin(angles[i]) - key_size / 2
        labels[i].place(x=x, y=y)
    
    root.after(speed, update_positions)  # Repeat

update_positions()  # Start animation
root.mainloop()





