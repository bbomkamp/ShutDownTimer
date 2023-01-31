import tkinter as tk

# Initiallize app (Init Window Object)
root = tk.Tk()
root.title("Shut Down Timer")
root.eval("tk::PlaceWindow . center") # Centers Window at Launch.

frame1 = tk.Frame(root, width=600, height=400, bg="#3d6466")
frame1.grid(row=0, column=0)

# Run app (Display Window)
root.mainloop()