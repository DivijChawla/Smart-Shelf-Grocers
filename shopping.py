import tkinter as tk
from tkinter import ttk, Button, Label
from PIL import Image, ImageTk
import sys 

import mysql.connector
from datetime import datetime

from Login_Button import logged_in_username


mydb = mysql.connector.connect(
    host="localhost",       # Your MySQL host 
    user="root",            # Your MySQL username
    password="root"         # Your MySQL password
)

mycursor = mydb.cursor()

# Function to create the database if it doesn't exist
def create_database():
    mycursor.execute("SHOW DATABASES LIKE 'smart_shelf_grocer'")
    result = mycursor.fetchone()
    if not result:
        mycursor.execute("CREATE DATABASE smart_shelf_grocer")
        mycursor.execute("USE smart_shelf_grocer")
    else:
        mycursor.execute("USE smart_shelf_grocer")

# Call the function to check and create the database
create_database()



# Function to create the transactions table if it doesn't exist
def create_transactions_table():
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        Trans_ID INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        item VARCHAR(255),
        quantity INT,
        total_price DECIMAL(10, 2),
        transaction_date DATE,   
        transaction_time TIME,
        PRIMARY KEY(Trans_ID,username)

    )
    """) 
    #note, curdate() is the same as current_date()
    mydb.commit()

# Call the function to ensure table is created
create_transactions_table()


items = [
    {"title": "Apple", "price": 10, "image": r"images/apple.jpeg"},
    {"title": "Banana", "price": 20, "image": r"images/banana.jpeg"},
    {"title": "Broccoli", "price": 30, "image": r"images/broccoli.jpeg"},
    {"title": "Carrots", "price": 40, "image": r"images/carrot.jpeg"},
    {"title": "Cucumbers", "price": 50, "image": r"images/cucumber.jpeg"},
    {"title": "Grapes", "price": 60, "image": r"images/grapes.jpeg"},
    {"title": "Orange", "price": 70, "image": r"images/orange.jpeg"},
    {"title": "Pineapple", "price": 80, "image": r"images/pineapple.jpeg"},
    {"title": "Strawberry", "price": 90, "image": r"images/strawberry.jpeg"},
    {"title": "Tomato", "price": 100, "image": r"images/tomato.jpeg"}
]


def create_item_frame(parent, item):
    frame = ttk.Frame(parent)
    item['count'] = tk.IntVar(value=0)

    # Load image
    image = Image.open(item["image"])
    image = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    label_image = ttk.Label(frame, image=photo)
    label_image.image = photo
    label_image.pack()

    label_title = ttk.Label(frame, text=item["title"], font=("Helvetica", 14))
    label_title.pack()

    label_price = ttk.Label(frame, text=f"₹{item['price']}", font=("Helvetica", 12, "bold"))
    label_price.pack()

    button_increase = ttk.Button(frame, text="+", command=lambda: increase(item))
    button_increase.pack(side="right")

    count_label = ttk.Label(frame, textvariable=item['count'])
    count_label.pack(side="right")

    button_decrease = ttk.Button(frame, text="-", command=lambda: decrease(item))
    button_decrease.pack(side="left")

    return frame

def increase(item):
    item['count'].set(item['count'].get() + 1)
    update_cart_button()

def decrease(item):
    count = item['count'].get()
    if count > 0:
        item['count'].set(count - 1)
    update_cart_button()

def update_cart_button():
    total_items = sum(item['count'].get() for item in items)
    cart_button.config(text=f"Cart ({total_items})")

def show_cart():
    global root
    root.destroy()  # This will close the main window

    cart_window = tk.Tk()
    cart_window.title("Cart")
    cart_window.geometry("800x600")

    cart_frame = ttk.Frame(cart_window, padding=20)
    cart_frame.pack(expand=True)

    # Create labels for listboxes
    ttk.Label(cart_frame, text="Items", font=("Helvetica", 14, "bold")).grid(row=0, column=0, padx=10, pady=5)
    ttk.Label(cart_frame, text="Quantity", font=("Helvetica", 14, "bold")).grid(row=0, column=1, padx=10, pady=5)
    ttk.Label(cart_frame, text="Price", font=("Helvetica", 14, "bold")).grid(row=0, column=2, padx=10, pady=5)

    listbox_items = tk.Listbox(cart_frame, font=("Helvetica", 14), height=15, width=20)
    listbox_quantity = tk.Listbox(cart_frame, font=("Helvetica", 14), height=15, width=10)
    listbox_total_price = tk.Listbox(cart_frame, font=("Helvetica", 14), height=15, width=15)

    listbox_items.grid(row=1, column=0, padx=10, pady=5)
    listbox_quantity.grid(row=1, column=1, padx=10, pady=5)
    listbox_total_price.grid(row=1, column=2, padx=10, pady=5)

    total_items = sum(item['count'].get() for item in items)
    total_price = sum(item['count'].get() * item['price'] for item in items)

    for item in items:
        if item['count'].get() > 0:
            listbox_items.insert(tk.END, item['title'])
            listbox_quantity.insert(tk.END, item['count'].get())
            listbox_total_price.insert(tk.END, f"₹{item['count'].get() * item['price']}")

    total_items_label = ttk.Label(cart_frame, text=f"Total Items: {total_items}", font=("Helvetica", 16, "bold"))
    total_items_label.grid(row=2, column=0, columnspan=2, pady=10)

    total_price_label = ttk.Label(cart_frame, text=f"Total Price: ₹{total_price}", font=("Helvetica", 16, "bold"))
    total_price_label.grid(row=2, column=2, pady=10)

    proceed_button = ttk.Button(cart_frame, text="Proceed to Pay", command=lambda: proceed_to_pay(cart_window))
    proceed_button.grid(row=3, column=2, sticky='e', pady=20)

def proceed_to_pay(cart_window):
    cart_window.destroy()

    # Assuming `logged_in_username` is passed or globally accessible
    global logged_in_username  

    # Insert the transaction details into the database
    for item in items:
        if item['count'].get() > 0:
            item_title = item['title']
            item_quantity = item['count'].get()
            total_item_price = item_quantity * item['price']
            transaction_date = datetime.now().date()
            transaction_time = datetime.now().time()

            # Insert transaction data into the MySQL database
            
            mycursor.execute(
                "INSERT INTO transactions (username, item, quantity, total_price, transaction_date, transaction_time) VALUES (%s, %s, %s, %s, %s, %s)",
                (logged_in_username, item_title, item_quantity, total_item_price, transaction_date, transaction_time)
            )
            mydb.commit()

    def endit():
        thankyou.destroy()
        sys.exit('Program Ended')

    # Create the main Tkinter window for the "Thank You" screen
    thankyou = tk.Tk()
    thankyou.geometry("830x830")
    thankyou.title("Thank you!")
    thankyou.configure(background='#ADD8E6')

    # Close button to end the program
    close_button = Button(thankyou, text="Close", command=endit, height=2, width=10)
    close_button.pack(side="bottom", padx=5, pady=10)

    # Display a "Thank You" image
    global img
    global img_tk
    img = Image.open("images/smart shelf groceries.png")
    img = img.resize((600, 800), Image.BICUBIC)
    img_tk = ImageTk.PhotoImage(img)
    panel = Label(thankyou, image=img_tk, bg="#ADD8E6")
    panel.pack(side="top", fill="both", expand="yes")

    thankyou.mainloop()

def search_items(*args):
    search_query = search_var.get().lower()
    for widget in items_frame.winfo_children():
        widget.destroy()

    filtered_items = [item for item in items if search_query in item["title"].lower()]
    display_items(filtered_items)

def display_items(display_items):
    columns_per_row = 5
    current_row_frame = None

    for idx, item in enumerate(display_items):
        if idx % columns_per_row == 0:
            current_row_frame = ttk.Frame(items_frame)
            current_row_frame.pack(fill='x', pady=5)

        item_frame = create_item_frame(current_row_frame, item)
        item_frame.pack(side='left', padx=10, pady=5)

root = tk.Tk()
root.title("Shopping Window")
root.geometry("1200x1000")  # Change this line to set the default size

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

title_label = ttk.Label(main_frame, text="Items for Sale", font=("Helvetica", 18))
title_label.pack(pady=10)

search_cart_frame = ttk.Frame(main_frame)
search_cart_frame.pack(pady=10)

search_var = tk.StringVar()
search_var.trace_add("write", search_items)

search_bar = ttk.Entry(search_cart_frame, textvariable=search_var, width=50)
search_bar.pack(side="left", padx=(0, 10))

cart_button = ttk.Button(search_cart_frame, text="Cart (0)", command=show_cart)
cart_button.pack(side="left")

canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

items_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=items_frame, anchor="nw")

display_items(items)

root.mainloop()
