#Importing tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#Exit command to exit
def exit_command():
    root.destroy()
    
#Continue to next page
def continue_command():
    root.destroy()
    import Login_Button
root = Tk()
root.geometry("650x650")
root.title("Smart Shelf Groceries")
root.configure(background='#ADD8E6')

# Load and display the image
img = ImageTk.PhotoImage(Image.open("images/icon.png"))
panel = Label(root, image=img, bg='#ADD8E6')
panel.pack(side="top", fill="both", expand="yes")

# Create button frame
button_frame = Frame(root, bg='#ADD8E6')
button_frame.pack(side="bottom", fill="x", padx=8, pady=8)

# Continue button
continue_button = ttk.Button(button_frame, text="Continue", command=continue_command,default="active")
continue_button.pack(side="right", padx=8)

# Exit button
exit_button = ttk.Button(button_frame, text="Exit", command=exit_command)
exit_button.pack(side="right", padx=8)


root.mainloop()


