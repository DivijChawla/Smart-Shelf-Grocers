import tkinter as tk
from tkinter import ttk, Entry, Listbox, Button, Label
import csv
from PIL import Image, ImageTk
import checkout


def update(data):
    my_list.delete(0, tk.END)
    for item in data:
        my_list.insert(tk.END, item)

def fillout(e):
    my_entry.delete(0, tk.END)
    my_entry.insert(0, my_list.get(tk.ANCHOR))

def check(e):
    typed = my_entry.get()
    if typed == '':
        data = fruits
    else:
        data = [item for item in fruits if typed.lower() in item.lower()]
    update(data)

def select():
    selected_item = my_list.get(tk.ANCHOR)
    display_selected_item(selected_item)

def display_selected_item(item):
    item_name_label.config(text="Item Name: " + item)
    selected_item = next((x for x in selected_items if x["name"] == item), None)

    if selected_item:
        selected_item['quantity'] += 1
        selected_item['price'] = prices[item] * selected_item['quantity']
    else:
        selected_items.append({"name": item, "quantity": 1, "price": prices[item]})
        selected_item = selected_items[-1]

    quantity_entry.delete(0, tk.END)
    quantity_entry.insert(0, selected_item['quantity'])
    update_price(selected_item['quantity'])

def update_price_entry(event):
    try:
        quantity = int(quantity_entry.get())
        update_price(quantity)
    except ValueError:
        price_label.config(text="Price: Invalid Quantity")

def update_price(quantity):
    selected_item_name = my_list.get(tk.ANCHOR)
    if selected_item_name in prices:
        price = prices[selected_item_name] * quantity
        price_label.config(text="Price: " + str(price))
    else:
        price_label.config(text="Price: Item not found")

def save_selected_items():
    try:
        quantity = int(quantity_entry.get())
        update_price(quantity)
    except ValueError:
        price_label.config(text="Price: Invalid Quantity")

    item_name = my_list.get(tk.ANCHOR)
    selected_item = next((x for x in selected_items if x["name"] == item_name), None)

    if selected_item:
        selected_item['quantity'] = quantity
        selected_item['price'] = prices[item_name] * quantity
    else:
        selected_items.append({"name": item_name, "quantity": quantity, "price": prices[item_name]})
        selected_item = selected_items[-1]

    update_selected_items_label()

    save_to_csv(selected_items)

def update_selected_items_label():
    selected_items_text = ""
    for item in selected_items:
        selected_items_text += f"Item: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']} RS\n"
    my_Label.config(text=selected_items_text.strip())

def save_to_csv(items):
    with open('selected_items.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Item Name", "Quantity", "Price"])
        for item in items:
            csvwriter.writerow([item['name'], item['quantity'], item['price']])


def cont():
    root.withdraw()
    checkout.display_checkout(selected_items)


root = tk.Tk()
root.geometry("800x600")
root.title("Grocery Shopping")

root.configure(background='#ADD8E6')

style = ttk.Style()
style.configure("TFrame", background='#ADD8E6')

# Left Section
left_frame = ttk.Frame(root, style="TFrame")
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

my_label = ttk.Label(left_frame, text="Choose your groceries!", font=("Helvetica", 14), foreground="grey")
my_label.pack(pady=20)

my_entry = Entry(left_frame, font=("Helvetica", 20))
my_entry.pack()

my_list = Listbox(left_frame, width=50)
my_list.pack(pady=40)

fruits = [
    "Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry",
    "Orange", "Olive"
]

update(fruits)

my_list.bind("<Button-1>", fillout)
my_entry.bind("<KeyRelease>", check)

my_button2 = Button(left_frame, text='Select', command=select, font=("Helvetica", 16))
my_button2.pack()

# Right Section
right_frame = ttk.Frame(root, style="TFrame")
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

item_name_label = ttk.Label(right_frame, text="Item Name: ")
item_name_label.grid(row=0, column=0, pady=10, sticky=tk.W)

quantity_label = ttk.Label(right_frame, text="Quantity:")
quantity_label.grid(row=1, column=0, pady=10, sticky=tk.W)
quantity_entry = Entry(right_frame, font=("Helvetica", 16))
quantity_entry.grid(row=1, column=1, pady=10, sticky=tk.W)

price_label = ttk.Label(right_frame, text="Price: ")
price_label.grid(row=2, column=0, pady=10, sticky=tk.W)

save_button = Button(right_frame, text='Save', command=save_selected_items, font=("Helvetica", 14))
save_button.grid(row=3, column=0, columnspan=2, pady=10)

selected_items_label = ttk.Label(right_frame, text="Selected Items:")
selected_items_label.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky=tk.W)
my_Label = ttk.Label(right_frame, text=' ')
my_Label.grid(row=5, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)

prices = {
    "Apple": 10,
    "Apricot": 20,
    "Avocado": 50,
    "Banana": 10,
    "Blackberry": 20,
    "Blueberry": 30,
    "Orange": 20,
    "Olive": 50
}

selected_items = []

quantity_entry.bind("<KeyRelease>", update_price_entry)

cart_button = Button(right_frame, text="Proceed To Cart", command=cont, font=("Helvetica", 12))
cart_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
