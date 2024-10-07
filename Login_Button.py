#Importing tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv

loginpage = Tk()
loginpage.geometry("650x650")
loginpage.title("Main Window")
loginpage.configure(background='#ADD8E6')

#Command when user clicks on register
def register():
    def save_credentials():
        username = username_entry.get()
        password = password_entry.get()

        with open("credentials.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:
                    messagebox.showerror("Registration Error", "Username already exists. Please choose another.")
                    return
        global logged_in_username
        logged_in_username = username 
        
        with open("credentials.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        messagebox.showinfo("Registration Successful", "Registration successful for user: {}".format(username))
        register_window.destroy()
        loginpage.destroy()
        import shopping

    def update_strength_bar(*args):
        password = password_var.get()

        if len(password) < 6:
            strength_bar.config(bg="red", text="Weak")
        elif len(password) < 10:
            strength_bar.config(bg="orange", text="Moderate")
        else:
            strength_bar.config(bg="green", text="Strong")

    global register_window
    register_window = Toplevel(loginpage)
    register_window.configure(background='#ADD8E6')
    register_window.title("Register")
    register_window.geometry("300x250")

    Label(register_window, text="Username:").pack(pady=10)
    username_entry = Entry(register_window)
    username_entry.pack()

    Label(register_window, text="Password:").pack(pady=10)
    password_var = StringVar()
    password_var.trace_add("write", update_strength_bar)
    password_entry = Entry(register_window, show="*", textvariable=password_var)
    password_entry.pack()

    strength_bar = Label(register_window, text="Password Strength", bg="gray")
    strength_bar.pack(pady=10)

    save_button = Button(register_window, text="Save", command=save_credentials, font=("Helvetica", 14))
    save_button.pack(pady=10)

register_button = Button(loginpage, text="Register", command=register, font=("Helvetica", 16))
register_button.pack(side=TOP, pady=(200, 10))

or_label = ttk.Label(loginpage, text="OR", font=("Helvetica", 14, "bold"))
or_label.pack(pady=20)

#Command when user clicks on login
def login():
    def check_credentials():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        with open("credentials.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == entered_username and row[1] == entered_password:
                    messagebox.showinfo("Login Successful", "Welcome, {}".format(entered_username))

                    global logged_in_username
                    logged_in_username = entered_username

                    loginpage.destroy()
                    import shopping
                    return

        messagebox.showerror("Login Failed", "Invalid username or password")

        username_entry.delete(0, END)
        password_entry.delete(0, END)

    global login_window
    login_window = Toplevel(loginpage)
    login_window.configure(background='#ADD8E6')
    login_window.title("Login")
    login_window.geometry("300x200")

    Label(login_window, text="Username:").pack(pady=10)
    username_entry = Entry(login_window)
    username_entry.pack()

    Label(login_window, text="Password:").pack(pady=10)
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    login_button = Button(login_window, text="Login", command=check_credentials, font=("Helvetica", 16))
    login_button.pack(pady=10)

login_button = Button(loginpage, text="Login", command=login, font=("Helvetica", 16))
login_button.pack(side=TOP, pady=(10, 200))



loginpage.mainloop()
