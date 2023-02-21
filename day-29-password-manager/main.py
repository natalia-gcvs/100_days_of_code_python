from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_NAME = 'Courier'


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
        password_entry.insert(0, string=password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_entries():
    website_w = website_entry.get()
    username_w = username_entry.get()
    password_w = password_entry.get()

    if website_w == "" or password_w == "":
        messagebox.showwarning(title='Ooops', message="Please, don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_w, message=f'These are the details entered: \nEmail: {username_w}\n'
                                                        f'Password: {password_w}')
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{website_w} | {username_w} | {password_w}\n")
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

#Labels
website = Label(text='Website:')
website.grid(column=0, row=1)
username = Label(text='Email/Username:')
username.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky='ew')
website_entry.focus()
username_entry = Entry(width=35)
username_entry.insert(0, 'natalia@gmail.com')
username_entry.grid(column=1, row=2, columnspan=2, sticky='ew')
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='ew')


#Buttons
password_button = Button(text='Generate password', command=generate_password)
password_button.grid(column=2, row=3, sticky='ew')
add_button = Button(text='Add', width=36, command=get_entries)
add_button.grid(column=1, row=4, columnspan=2, sticky='ew')


window.mainloop()
