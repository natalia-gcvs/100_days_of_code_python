from tkinter import *


def converter():
    miles = int(entry.get())
    km = round(miles*1.61, 2)
    conversion_label.config(text=km)


window = Tk()
window.title('Mile to Km Converter')
window.config(pady=30, padx=50)


# Entry

entry = Entry(width=10)
entry.grid(column=1, row=0)

# Miles Label

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

# is equal to label

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

# conversion label

conversion_label = Label(text='')
conversion_label.grid(column=1, row=1)

# Km Label

km_label= Label(text='Km')
km_label.grid(column=2, row=1)

# calculate button

calculate_button = Button(text='Calculate', command=converter)
calculate_button.grid(column=1, row=2)

window.mainloop()