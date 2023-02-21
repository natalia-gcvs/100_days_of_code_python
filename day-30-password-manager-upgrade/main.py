from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = 'Courier'

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    try:
        website = website_entry.get()
        with open('data.json', 'r') as file:
            dictionary = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title='Error', message='No Data File Found.')
    else:
        if website in dictionary:
            messagebox.showinfo(title=website, message=f"Email: {dictionary[website]['email']}\n"
                                                   f"Password: {dictionary[website]['password']}")
        else:
            messagebox.showwarning(title='Error', message='Website not found.')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]

    password_list += [choice(symbols) for char in range(randint(2, 4))]

    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)

    password_w = password_entry.get()

    password_entry.insert(0, string=password)

    if password_w != '':
        password_entry.delete(0, END)
        generate_password()

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_entries():
    website_w = website_entry.get()
    username_w = username_entry.get()
    password_w = password_entry.get()

    new_data = {
        website_w:{
            "email": username_w,
            "password": password_w,
        }
    }

    if website_w == "" or password_w == "":
        messagebox.showwarning(title='Ooops', message="Please, don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as file:
                #Reading the old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
                # Saving updated data
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        # else:
        #     # Updating old data with new data
        #     data.update(new_data)
        #     # Saving updated data
        #     with open('data.json', 'w') as file:
        #         json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website = Label(text='Website:')
website.grid(column=0, row=1)
username = Label(text='Email/Username:')
username.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky='ew')
website_entry.focus()
username_entry = Entry(width=35)
username_entry.insert(0, 'natalia@gmail.com')
username_entry.grid(column=1, row=2, columnspan=2, sticky='ew')
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='ew')


# Buttons
search_button = Button(text='Search', command=search_website)
search_button.grid(column=2, row=1, sticky='ew')
password_button = Button(text='Generate password', command=generate_password)
password_button.grid(column=2, row=3, sticky='ew')
add_button = Button(text='Add', width=36, command=get_entries)
add_button.grid(column=1, row=4, columnspan=2, sticky='ew')


window.mainloop()
