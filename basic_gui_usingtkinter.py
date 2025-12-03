
import tkinter as tk
from tkinter import ttk
import datetime

def ts():
    return datetime.datetime.now().strftime("%H:%M:%S")

# ---- Simple logger helper ----
def log(msg):
    log_box.insert(0, f"[{ts()}] {msg}")
    # keep log short
    if log_box.size() > 20:
        log_box.delete(20, tk.END)

# ---- Event handlers ----
def on_click(e):
    log(f"Mouse Click at ({e.x},{e.y})")

def on_double(e):
    log(f"Mouse Double-Click at ({e.x},{e.y})")

def on_enter(e):
    log("Mouse Enter")

def on_leave(e):
    log("Mouse Leave")

def on_keypress(e):
    log(f"KeyPress: keysym={e.keysym} char={repr(e.char)}")

def on_keyrelease(e):
    log(f"KeyRelease: keysym={e.keysym}")

def on_return(e):
    log("Return (Enter) pressed")
    next_slide()
    return "break"

def on_focus_in(e):
    log("Entry FocusIn")

def on_focus_out(e):
    log("Entry FocusOut")

def on_resize(e):
    # e.widget is root window; ignore small irrelevant Configure calls for other widgets
    if e.widget == root:
        log(f"Window resized to {e.width}×{e.height}")

def on_close():
    log("Window close requested; exiting.")
    root.destroy()

# ---- Small keyboard-definition slides ----
slides = [
    ("KeyPress", "Fired when a physical key is pressed."),
    ("KeyRelease", "Fired when a physical key is released."),
    ("Return (Enter)", "Specific event for the Enter/Return key."),
    ("Importance", "Keyboard events capture user input & shortcuts.")
]
slide_index = 0
def show_slide():
    title_var.set(slides[slide_index][0])
    text_var.set(slides[slide_index][1])
def next_slide():
    global slide_index
    slide_index = (slide_index + 1) % len(slides)
    show_slide()
def prev_slide():
    global slide_index
    slide_index = (slide_index - 1) % len(slides)
    show_slide()

# ---- UI ----
root = tk.Tk()
root.title("Simple Events (small demo)")
root.geometry("700x320")
root.minsize(500,300)

# Left: interactive area
left = ttk.Frame(root, padding=8)
left.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)

canvas = tk.Canvas(left, bg="#fff0f3", height=180, relief="ridge", bd=2)
canvas.pack(fill="both", expand=True)
canvas.create_text(150, 90, text="Click / Double-click\nMove mouse in/out", font=("Arial", 12))

# Bind mouse events
canvas.bind("<Button-1>", on_click)
canvas.bind("<Double-Button-1>", on_double)
canvas.bind("<Enter>", on_enter)
canvas.bind("<Leave>", on_leave)

# Entry to capture keyboard & focus
entry = ttk.Entry(left)
entry.pack(fill="x", pady=8)
entry.insert(0, "Type here and press Enter")
entry.bind("<KeyPress>", on_keypress)
entry.bind("<KeyRelease>", on_keyrelease)
entry.bind("<Return>", on_return)
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)

# Right: log and slides
right = ttk.Frame(root, padding=8, width=260)
right.grid(row=0, column=1, sticky="nsew")
right.grid_propagate(False)

ttk.Label(right, text="Event Log (latest top)").pack(anchor="w")
log_box = tk.Listbox(right, height=12)
log_box.pack(fill="both", pady=4)

# Slides for keyboard event definitions
title_var = tk.StringVar()
text_var = tk.StringVar()
ttk.Label(right, textvariable=title_var, font=("Arial", 10, "bold")).pack(anchor="w", pady=(6,0))
ttk.Label(right, textvariable=text_var, wraplength=240).pack(anchor="w", pady=(2,6))

nav = ttk.Frame(right)
nav.pack(fill="x")
ttk.Button(nav, text="Prev", command=prev_slide).pack(side="left")
ttk.Button(nav, text="Next", command=next_slide).pack(side="right")

# Window events
root.bind("<Configure>", on_resize)
root.protocol("WM_DELETE_WINDOW", on_close)

show_slide()
log("App started — interact with the canvas and entry")

root.mainloop()
