import tkinter as tk
import time
import os

# Initialize app (Initialize Window Object)
root = tk.Tk()
root.title("Shut Down Timer")
root.geometry("600x400")
root.eval("tk::PlaceWindow . center")  # Centers Window at Launch.

frame1 = tk.Frame(root, bg="#3d6466")
frame1.pack(fill="both", expand=True)

# Add Entry widget for user input
time_entry = tk.Entry(frame1)
time_entry.pack(pady=10)

# Add a button to start the countdown
start_button = tk.Button(frame1, text="Start", command=root.quit)
start_button.pack(pady=10)

def countdown():
    time = int(time_entry.get())

    if time <= 0:
        os.system("shutdown /s /t 1")
    else:
        # Update the UI with the new time
        time_entry.config(state="normal")
        time_entry.delete(0, "end")
        time_entry.insert(0, time)
        time_entry.config(state="readonly")

        # Schedule the next iteration of the countdown
        root.after(1000, countdown, time - 1)

# Run app (Display Window)
root.mainloop()

# Start the countdown after the user has entered the time
countdown()
