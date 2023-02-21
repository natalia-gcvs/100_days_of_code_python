import tkinter
from tkinter import *



window = Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# Label

my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label['text'] = 'Trying a new label'
my_label.config(text='New label')
my_label.grid(column=0, row=0)

# Entry

entry = Entry(width=10)
entry.grid(column=3, row=2)

# Button

def button_clicked():
    new_entry = entry.get()
    my_label.config(text=new_entry)

my_button = Button(text='click me', command=button_clicked)
my_button.grid(column=1, row=1)

# new Button

new_button = Button(text='new button')
new_button.grid(column=2, row=0)

# Scale
# Called with current scale value
# def scale_used(value):
#     value1 = scale.get()
#     print(value1)
#
# scale = Scale(from_=0, to=20, command=scale_used)
# scale.pack()


window.mainloop()

