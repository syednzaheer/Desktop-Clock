import tkinter as ui
import time

# Display Name
DISPLAY_NAME = "My Desktop"

# Colors
BACKGROUND_COLOR = "#010101"  # Used for Transparency
TEXT_COLOR_MAIN = "#E0E0E0"
TEXT_COLOR_SUB = "#707070"

window = ui.Tk()

# No Borders

window.overrideredirect(True)

# Center it Near the Top

window_width = 374
window_height = 135
screen_width = window.winfo_screenwidth()
x_position = int((screen_width - window_width) / 2)
y_position = 20

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Make it Transparent

window.config(bg=BACKGROUND_COLOR)
window.attributes("-transparentcolor", BACKGROUND_COLOR)

def update_clock():

    # Update Time

    time_text = time.strftime("%I:%M:%S %p")
    digital_clock_lbl.config(text=time_text)
    
    # Loop every Second

    digital_clock_lbl.after(1000, update_clock)

# Time Display

digital_clock_lbl = ui.Label(
    window,
    text="00:00:00",
    font=("Garamond", 55, "bold"),
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR_MAIN,
    width=12,
    bd=0,
    highlightthickness=0
)
digital_clock_lbl.pack()

# Name Label

name_lbl = ui.Label(
    window,
    text=DISPLAY_NAME,
    font=("Times New Roman", 30, "bold"),
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR_SUB,
    bd=0,
    highlightthickness=0
)
name_lbl.pack(fill='x', anchor='center')

# Keep it Behind Windows

window.lower()
window.attributes("-topmost", False)

update_clock()
window.mainloop()
