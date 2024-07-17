from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# standard dialog is the message boxes in tkinter
# most popular is tkMessageBox
# "showinfo", "showwarning", "showerror",
#            "askquestion", "askokcancel", "askyesno",
#            "askyesnocancel", "askretrycancel"

# pyperclip save to clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters)) for nr_letters in range(random.randint(8, 10))]
    [password_list.append(random.choice(numbers)) for nr_numbers in range(random.randint(2, 4))]
    [password_list.append(random.choice(symbols)) for nr_symbols in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    # print(f"Your password is: {password}")

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_search = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
        return
    else:
        if website_search in data:
            dict_email = data[website_search]["email"]
            dict_password = data[website_search]["password"]
            messagebox.showinfo(title=website_search, message=f"{dict_email}\n{dict_password}")
        else:
            messagebox.showinfo(title=website_search, message=f"No details for {website_search} exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_to_file():
    website_text = website_input.get()
    email_text = email_user_input.get()
    password_text = password_input.get()
    new_data = {website_text: {
        "email": email_text,
        "password": password_text,
    }
    }

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Check", message="Please enter the input in all the fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

            # read old data
            # update old data with new data
            # saving data


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
# use canvas.pack() initially then move to the grid
canvas.grid(column=1, row=0)

# columnspan

# Labels
website = Label(text="Website: ")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username: ")
email_username.grid(column=0, row=2)

password = Label(text="Password: ")
password.grid(column=0, row=3)

# result = Label(text="")
# result.grid(column=1, row=5)

# input boxes
website_input = Entry(window, width=35)
website_input.grid(column=1, row=1, sticky="EW")
# website_input_data = StringVar()
website_input.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

email_user_input = Entry(window, width=35)
email_user_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_user_input.insert(0, "example@email.com")
# email_user_input_data = StringVar()

password_input = Entry(window, width=21)
password_input.grid(column=1, row=3, sticky="EW")
# password_input_data = StringVar

# buttons
generate_pass = Button(text="Generate Password", command=password_generator)
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=write_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
