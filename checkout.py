import csv
from tkinter import *
from PIL import Image, ImageTk


def display_checkout(selected_items):
    checkout_window = Tk()
    checkout_window.title("Checkout")
    checkout_window.configure(background='#ADD8E6')

    checkout_label = Label(checkout_window,
                           text="Checkout",
                           font=("Helvetica", 16))
    checkout_label.grid(row=0, column=0, columnspan=3, pady=10)

    checkout_listbox = Listbox(checkout_window,
                               width=50,
                               height=10,
                               font=("Helvetica", 12))
    checkout_listbox.grid(row=1, column=0, columnspan=3, pady=10)

    total_price = 0

    for item in selected_items:
        item_name = item['name']
        quantity = item['quantity']
        price = item['price']
        total_price += price

        checkout_text = "Item: " + item_name + " | Quantity: " + str(quantity) + " | Price: " + str(price) + " RS"

        checkout_listbox.insert(END, checkout_text)

    total_price_label = Label(checkout_window,
                              text=f"Total Price: {total_price} RS",
                              font=("Helvetica", 12))
    total_price_label.grid(row=2, column=0, columnspan=2, pady=10, sticky=W)

    save_button = Button(checkout_window,
                         text='Proceed to Pay',
                         command=lambda: proceed_to_pay(selected_items, checkout_window))
    save_button.grid(row=2, column=2, pady=10, sticky=E)

    checkout_window.mainloop()


def proceed_to_pay(items, checkout_window):
    with open('selected_items_checkout.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Item Name", "Quantity", "Price"])
        for item in items:
            csvwriter.writerow([item['name'], item['quantity'], item['price']])
    checkout_window.withdraw()
    thankyou = Tk()
    thankyou.geometry("900x1400")
    thankyou.title("Thank you!")
    thankyou.configure(background='#ADD8E6')
    img = ImageTk.PhotoImage(Image.open("smart shelf groceries.png"))
    panel = Label(thankyou, image=img, bg='#ADD8E6')
    panel.pack(side="top", fill="both", expand="yes")
    thankyou.mainloop()


# if __name__ == "__main__":
#     selected_items = [
#         {
#             "name": "Apple",
#             "quantity": 2,
#             "price": 20
#         },
#         {
#             "name": "Banana",
#             "quantity": 1,
#             "price": 10
#         },
#         # Add more sample items if needed
#     ]

#     display_checkout(selected_items)
