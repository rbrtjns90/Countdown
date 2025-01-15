import tkinter as tk
import time
import threading
from itertools import cycle

def countdown_timer(seconds):
    """
    Runs a countdown timer for the specified number of seconds 
    """
    def update_timer():
        nonlocal seconds
        while seconds >= 0:
            # Update the timer text
            timer_label.config(text=f"{seconds}")
            seconds -= 1
            time.sleep(1)
        
        # Exit the overlay when the countdown finishes
        root.destroy()

    def flame_effect():
        """
        Updates the text color to simulate a flame effect.
        """
        for color in flame_colors:
            timer_label.config(fg=color)
            time.sleep(0.1)

    def animate_flame():
        """
        Animates the flame effect in a separate thread.
        """
        while True:
            flame_effect()

    # Start the timer update in a separate thread
    threading.Thread(target=update_timer, daemon=True).start()
    # Start the flame effect in a separate thread
    threading.Thread(target=animate_flame, daemon=True).start()

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")
root.attributes("-fullscreen", True)  # Fullscreen overlay
root.attributes("-topmost", True)  # Always on top
root.attributes("-alpha", 0.5)  # Transparency level (0.0 to 1.0)

# Set up a transparent background
root.configure(bg="black")

# Define flame colors
flame_colors = cycle(["red", "orange", "yellow", "orange"])

# Create the timer label
timer_label = tk.Label(root, text="", font=("Helvetica", 120, "bold"), bg="black")
timer_label.pack(expand=True)

# Start the countdown (e.g., 10 seconds)
countdown_timer(10)

# Run the application
root.mainloop()