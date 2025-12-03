# demo_tk_events.py
import tkinter as tk

def on_enter(e):
    # e.widget is the widget that triggered the event
    hover_label.config(text=f"Hovering: {e.widget.cget('text')}")

def on_leave(e):
    hover_label.config(text="Hovering: —")

def on_click(e):
    # single click: show which widget and mouse coords
    info_label.config(text=f"Single click on '{e.widget.cget('text')}' at ({e.x}, {e.y})")

def on_double_click(e):
    info_label.config(text=f"Double click! Widget='{e.widget.cget('text')}'")

def on_key(e):
    # show key symbol (use e.keysym for readable name)
    key_label.config(text=f"Key pressed: {e.keysym}")

def on_motion(e):
    # update coordinates of mouse over canvas
    coords_label.config(text=f"Mouse: ({e.x}, {e.y})")

root = tk.Tk()
root.title("Tkinter Events — RAM demo")
root.geometry("420x260")

# Top frame with buttons to demonstrate hover / clicks
top = tk.Frame(root, padx=8, pady=8)
top.pack(fill="x")

btn1 = tk.Button(top, text="Button A")
btn2 = tk.Button(top, text="Button B")
btn1.pack(side="left", padx=6)
btn2.pack(side="left", padx=6)

# Bind hover (Enter/Leave) and clicks to both buttons
for btn in (btn1, btn2):
    btn.bind("<Enter>", on_enter)                # mouse enters widget
    btn.bind("<Leave>", on_leave)                # mouse leaves widget
    btn.bind("<Button-1>", on_click)             # single left-click
    btn.bind("<Double-Button-1>", on_double_click)  # double left-click

# Middle area: a small canvas to show mouse motion coords
canvas = tk.Canvas(root, width=380, height=100, bg="white", relief="solid", bd=1)
canvas.pack(padx=8, pady=(0,8))

canvas.create_text(190, 10, text="Move mouse here →", anchor="n")
canvas.bind("<Motion>", on_motion)  # mouse movement over canvas

# Bottom info labels
hover_label = tk.Label(root, text="Hovering: —", anchor="w")
hover_label.pack(fill="x", padx=8)

coords_label = tk.Label(root, text="Mouse: (—, —)", anchor="w")
coords_label.pack(fill="x", padx=8)

info_label = tk.Label(root, text="Click info will appear here", anchor="w")
info_label.pack(fill="x", padx=8)

key_label = tk.Label(root, text="Key pressed: —", anchor="w")
key_label.pack(fill="x", padx=8, pady=(0,8))

# Application-level binding: capture key presses anywhere in the window
root.bind("<KeyPress>", on_key)

# Make sure the window receives key events: set focus to root
root.focus_set()

root.mainloop()
