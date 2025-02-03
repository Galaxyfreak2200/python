import tkinter as tk

window = tk.Tk()

window.title("limbo virus")
window.geometry("500x400")
window.resizable(False, False)


label = tk.Label(window, text="🔑🔑🔑🔑🔑🔑🔑🔑")
label.place(x=75, y=150)

label2 = tk.Label(window, text="Disclamer! This is not a real virus, This is my first python script!")
label2.place(x=75, y=75)



label.config(font=("Arial", 20))

window.mainloop()