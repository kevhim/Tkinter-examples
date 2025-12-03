import tkinter
from tkinter import *

# Create main window
root = Tk()
root.title("Simple Calculator")
root.configure(bg="#ffd1dc")  # Light pastel pink background

# Entry box (display)
entry = Entry(root, width=25, borderwidth=3, font=("Arial", 18),
              bg="#ffe6ee", fg="#333", insertbackground="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to add numbers/characters to display
def button_click(value):
    entry.insert(END, value)

# Function to clear the display
def clear():
    entry.delete(0, END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Common button style
btn_bg = "#ffb6c1"  # Light Pink
btn_fg = "#000"
btn_active = "#ff8da1"

# Create buttons using a loop
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=5, height=2, font=("Arial", 14),
               bg="#ff5c8a", fg="white", activebackground="#ff3c6f",
               command=calculate).grid(row=row, column=col, padx=2, pady=2)
    else:
        Button(root, text=text, width=5, height=2, font=("Arial", 14),
               bg=btn_bg, fg=btn_fg, activebackground=btn_active,
               command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=2, pady=2)

# Clear button
Button(root, text="C", width=22, height=2, font=("Arial", 14),
       bg="#ff9bb3", fg="white", activebackground="#ff6f91",
       command=clear).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()
