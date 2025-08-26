import tkinter as tk
from tkinter import *

coffee_machine = {
    "menu": {
        "espresso": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
            "sugar": 5,
            "cost": 2.0   # cost in dollars
        },
        "latte": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "sugar": 10,
            "cost": 3.5
        },
        "cappuccino": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "sugar": 8,
            "cost": 3.0
        }
    },
    "inventory": {
        "water": 1000,
        "milk": 500,
        "coffee": 300,
        "sugar": 200
    }
}

win = tk.Tk()
win.title("Coffee Machine")
win.geometry("800x600")
win.config(bg = "#6F4E37")

for i in range(7):
    win.rowconfigure(i, weight=1)
for j in range(3):
    win.columnconfigure(j, weight=1)

main_title = Label(text= "Ready for a coffee break? ", font=("Helvetica", 20),bg="#6F4E37", fg= "#F5F5DC")
main_title.grid(row=0,column=0, columnspan=3)

espresso_button = Button(text= "Espresso:\n$2.00 ", font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723")
espresso_button.grid(row=1,column=0)

latte_button = Button(text= "Latte:\n$3.50 ", font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723")
latte_button.grid(row=1,column=1)

cappuccino_button = Button(text= "Cappuccino:\n$3.00", font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723")
cappuccino_button.grid(row=1,column=2)

money_label = Label(text= "Enter your payment: ", font=("Helvetica", 14),bg="#6F4E37", fg= "#F5F5DC")
money_label.grid(row=2, column=0, columnspan=2)

money_entry = Entry(font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723", justify="center")
money_entry.grid(row=2, column=1,columnspan=2)

order_button = Button(text= "Start Brewing", font=("Helvetica", 14),bg="#D2B48C", fg= "#3E2723")
order_button.grid(row=3,column=0, columnspan=3)

win.mainloop()

