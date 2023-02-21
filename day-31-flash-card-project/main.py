from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice
import os

BACKGROUND_COLOR = "#B1DDC6"
current_choice = {}

path = 'data/new_data.csv'
file_exists = os.path.exists(path)

if file_exists:
    try:
        data = pd.read_csv(path)
    except ValueError:
        messagebox.showinfo(title='Congrats', message="We've learned all the words, time to add more!")
        os.remove(path)
    else:
        to_learn = data.to_dict(orient='records')
else:
    data = pd.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_choice, flip_timer
    window.after_cancel(flip_timer)
    current_choice = choice(to_learn)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_choice['French'], fill='black')
    flip_timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_choice)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv('data/new_data.csv', index=False)
    print(len(new_data))
    next_card()



#-----------------------------------FLIP CARD --------------------------------------------
def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_choice['English'], fill='white')


#-----------------------------------UI SETUP----------------------------------------------

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=530, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card = canvas.create_image(400, 265, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=("Ariel", 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)


cross_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

check_button = PhotoImage(file='images/right.png')
right_button = Button(image=check_button, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

try:
    next_card()
except NameError:
    window.destroy()

window.mainloop()





