import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("Coffee Machine")
win.geometry("800x600")
win.config(bg = "#6F4E37")

for i in range(7):
    win.rowconfigure(i, weight=1)
for j in range(3):
    win.columnconfigure(j, weight=1)

total_sales = 0
customer_order = ""
order_price = 0

coffee_machine = {
    "menu": {
        "espresso": {
            "water": 50.00,
            "milk": 0.00,
            "coffee": 18,
            "sugar": 5.00,
            "cost": 2.0
        },
        "latte": {
            "water": 200.00,
            "milk": 150.00,
            "coffee": 24.00,
            "sugar": 10.00,
            "cost": 3.5
        },
        "cappuccino": {
            "water": 250.00,
            "milk": 100.00,
            "coffee": 24.00,
            "sugar": 8.00,
            "cost": 3.0
        }
    },
    "inventory": {
        "water": 1000.00,
        "milk": 500.00,
        "coffee": 300.00,
        "sugar": 200.00
    }
}

def inventory_check(customer_choice):
    if (
            coffee_machine["menu"][customer_choice]["water"] <= coffee_machine["inventory"]["water"] and
            coffee_machine["menu"][customer_choice]["milk"] <= coffee_machine["inventory"]["milk"] and
            coffee_machine["menu"][customer_choice]["coffee"] <= coffee_machine["inventory"]["coffee"] and
            coffee_machine["menu"][customer_choice]["sugar"] <= coffee_machine["inventory"]["sugar"]
    ):
        return True
    else:
        return False

def update_order_status(cust_order,price):
    order_status.config(text=f"{cust_order} selected | Price: ${price:.2f} ")

def update_inventory(customer_choice):
    coffee_machine["inventory"]["water"] = coffee_machine["inventory"]["water"]  - coffee_machine["menu"][customer_choice]["water"]
    coffee_machine["inventory"]["milk"] =  coffee_machine["inventory"]["milk"] - coffee_machine["menu"][customer_choice]["milk"]
    coffee_machine["inventory"]["coffee"]  = coffee_machine["inventory"]["coffee"]  - coffee_machine["menu"][customer_choice]["coffee"]
    coffee_machine["inventory"]["sugar"] = coffee_machine["inventory"]["sugar"] - coffee_machine["menu"][customer_choice]["sugar"]

def order_espresso():
    global customer_order, order_price, warning_label
    customer_order = "espresso"
    order_price = float(coffee_machine["menu"][customer_order]["cost"])

    if not inventory_check(customer_order):
        warning_label.config(text="Unfortunately, we can’t prepare this drink. Please choose another.")
        win.after(2000, lambda: warning_label.config(text=""))

    else:
        update_order_status(customer_order,order_price)

def order_latte():
    global customer_order, order_price, warning_label
    customer_order = "latte"
    order_price = float(coffee_machine["menu"][customer_order]["cost"])

    if not inventory_check(customer_order):
        warning_label.config(text="Unfortunately, we can’t prepare this drink. Please choose another.")
        win.after(2000, lambda: warning_label.config(text=""))

    else:
        update_order_status(customer_order, order_price)

def order_cappuccino():
    global customer_order, order_price, warning_label
    customer_order = "cappuccino"
    order_price = float(coffee_machine["menu"][customer_order]["cost"])

    if not inventory_check(customer_order):
        warning_label.config(text="Unfortunately, we can’t prepare this drink. Please choose another.")
        win.after(2000, lambda: warning_label.config(text=""))

    else:
        update_order_status(customer_order, order_price)

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate_money():
    global customer_order, order_price, total_sales

    if customer_order == "":
        warning_label.config(text="Please select a drink first.")
        win.after(2000, lambda: warning_label.config(text=""))
        return

    try:
        money_paid = float(money_entry.get())   # convert to float
        order_price = coffee_machine["menu"][customer_order]["cost"]
        customers_change = money_paid - order_price

        if money_paid < order_price:
            warning_label.config(text=f"Insufficient amount paid. The price is ${order_price:.2f}.")
            win.after(2000, lambda: warning_label.config(text=""))

        else:
            money_entry.delete(0,"end")
            update_inventory(customer_order)
            total_sales += order_price
            order_status.config(text=f"Thank you for your order. Please wait while we prepare your {customer_order}.")
            if customers_change != 0:
                warning_label.config(text=f"Please don’t forget your change: ${customers_change:.2f}")
            win.after(3000, show_ready)

    except ValueError:
        warning_label.config(text="Please enter numbers only.")
        win.after(2000, lambda: warning_label.config(text=""))

def show_ready():
    global customer_order, order_price
    global order_status
    order_status.config(text=f"Your {customer_order} is ready. Please take your order. Enjoy your drink!")
    win.after(3000, lambda: (order_status.config(text=""), warning_label.config(text="")))
    customer_order = ""
    order_price = 0


main_title = Label(text= "Ready for a coffee break? ", font=("Helvetica", 20),bg="#6F4E37", fg= "#F5F5DC")
main_title.grid(row=0,column=0, columnspan=3)

espresso_button = Button(text= "Espresso", font=("Helvetica", 14), bg="#D2B48C", fg= "#3E2723", command=order_espresso)
espresso_button.grid(row=1,column=0)

latte_button = Button(text= "Latte", font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723", command=order_latte)
latte_button.grid(row=1,column=1)

cappuccino_button = Button(text= "Cappuccino", font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723", command=order_cappuccino)
cappuccino_button.grid(row=1,column=2)

money_label = Label(text= "Enter your payment: ", font=("Helvetica", 14),bg="#6F4E37", fg= "#F5F5DC")
money_label.grid(row=2, column=0, columnspan=2)

money_entry = Entry(font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723", justify="center")
money_entry.grid(row=2, column=1,columnspan=2)

order_button = Button(text= "Start Brewing", font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723", command=calculate_money)
order_button.grid(row=3,column=0, columnspan=3)

order_status = Label(font=("Helvetica", 17),bg="#6F4E37", fg= "#F5F5DC")
order_status.grid(row=4,column=0, columnspan=3)

warning_label = Label(font=("Helvetica", 17),bg="#6F4E37", fg= "#F5F5DC")
warning_label.grid(row=5,column=0, columnspan=3)

win.mainloop()

print(f"Total Sales: {total_sales}")
