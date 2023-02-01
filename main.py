import tkinter as tk
import os
import tkinter.ttk as ttk


def countdown(remaining_time, total_time):
    global after_id
    remaining_time -= 1

    # Calculate the remaining hours and seconds
    hours = remaining_time // 3600
    seconds = remaining_time % 3600
    minutes = seconds // 60
    seconds = seconds % 60

    # Update the remaining time label
    remaining_time_label.config(text="{} hours {} minutes {} seconds".format(hours, minutes, seconds))

    # Update the progress circle
    canvas.delete("all")
    canvas.create_arc(10, 10, 190, 190, start=90, extent=360*(remaining_time/total_time), fill="#16c5f5", width=2)


    if remaining_time <= 0:
        os.system("shutdown /s /t 1")
    else:
        # Schedule the next iteration of the countdown
        after_id = root.after(1000, countdown, remaining_time, total_time)

# Initialize app (Initialize Window Object)
root = tk.Tk()
root.title("Shut Down Timer")
# root.geometry("600x600")
# root.eval("tk::PlaceWindow . center")  # Centers Window at Launch.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to be 40% of the screen size
window_width = int(screen_width * 0.4)
window_height = int(screen_height * 0.4)
root.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)
root.geometry(f"+{window_x}+{window_y}")


frame1 = tk.Frame(root, bg="#3d6466")
frame1.pack(fill="both", expand=True)

# Add Entry widget for time input
time_entry = tk.Entry(frame1)
time_entry.pack(pady=10)

# Add Combobox widget for time type input
time_type = tk.StringVar()
time_type_combo = ttk.Combobox(frame1, textvariable=time_type, values=["minutes", "hours", "seconds"])
time_type_combo.current(0)
time_type_combo.pack(pady=10)

# Add a label to display the remaining time
remaining_time_label = tk.Label(frame1, text="", font=("TkDefaultFont", 14), bg="#3d6466", fg="white")
remaining_time_label.pack(pady=10)

# Add a canvas for the progress circle
canvas = tk.Canvas(frame1, width=200, height=200, bg="#3d6466", highlightthickness=0)
canvas.pack(pady=10)

after_id = None

def start_countdown():
    global after_id
    start_button.config(state=tk.DISABLED)  # Disable the start button
    time = int(time_entry.get())
    time_type = time_type_combo.get()

    if time_type == "minutes":
        time *= 60
    elif time_type == "hours":
        time *= 3600

    if time <= 0:
        os.system("shutdown /s /t 1")
    else:
        # Schedule the first iteration of the countdown
        after_id = root.after(1000, countdown, time, time)


# Add a button to start the countdown
start_button = tk.Button(frame1, text="Start", command=start_countdown)
start_button.pack(side="left", padx=100, pady=10)

def stop_countdown():
    global after_id
    start_button.config(state=tk.NORMAL)  # Enable the start button
    if after_id:
        root.after_cancel(after_id)
        after_id = None
        canvas.delete("all")
        remaining_time_label.config(text="")

# Add a button to cancel the countdown
cancel_button = tk.Button(frame1, text="Cancel", command=stop_countdown)
cancel_button.pack(side="right", padx=100, pady=10)


root.mainloop()
