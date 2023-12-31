from tkinter import *
import time
import datetime
import json

window = Tk()
window.geometry("600x330")
window.title("Password Manager")

raw_file = {}

## Functions :-


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    time_label.config(text=f"{hour}\n{minute}\n{second}")
    time_label.after(1000, clock)


def date():
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    day = datetime.datetime.today().day
    b = time.strftime("%b")
    a = (f"{day}\n{b}\n{year}")
    date_label.config(text=a)


# Application

def save_data():


    website_data = website_entry.get()
    password_data = password_entry.get()
    print(website_data)
    print(password_data)
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    raw_file.update({website_data: password_data})
    d_1 = json.dumps(raw_file)

    with open("file.json", mode="w") as file:
        file.write(d_1)
        s_1 = json.loads(d_1)
        s_2 = json.dumps(s_1)



def retrieve_data():
    with open("file.json", mode="w") as file:
        x = json.dumps(raw_file)
        y = json.loads(x)
        a = website_entry.get()
        b = y[a]
        password_entry.insert(0, b)

def clear_data():
    password_entry.delete(0, END)
    website_entry.delete(0, END)
# Design :-

website_entry = Entry(window, width=24, font=("Arial", 21))
website_entry.grid(row=1, column=1, columnspan=2, pady=40, padx=10)

password_entry = Entry(window, width=24, font=("Arial", 21))
password_entry.grid(row=2, column=1, columnspan=2, pady=10)

save_button = Button(text="Save", width=15, height=2, command=save_data)
save_button.grid(row=3, column=1, pady=10)

retrieve_button = Button(text="Retrieve", width=15, height=2, command=retrieve_data)
retrieve_button.grid(row=3, column=2, pady=10)

update_pass_button = Button(text="Clear", width=41, height=2, command= clear_data)
update_pass_button.grid(row=4, column=1, columnspan=2)

# Clock Module

time_label = Label(window, text="Hello", font=("Arial", 25), fg="green")
time_label.grid(row=1, column=3, padx=80, rowspan=2)

time_label.after(200, clock)

# Date Module

date_label = Label(window, text="Date", font=("Arial", 25), fg="green")
date_label.grid(row=3, column=3, padx=5, rowspan=4)

date_label.after(200, date)

window.mainloop()
