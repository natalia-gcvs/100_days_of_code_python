from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- RESET BUTTON ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    mark_label.config(text='')
    reps = 0

# ---------------------------- START BUTTON ------------------------------- #
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text='Timer', fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer
    count_min = count//60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count > 0:
        timer = window.after(1000, count_down, count -1)
        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    else:
        start()
        check_marks = ''
        work_sessions = reps//2
        for _ in range(work_sessions):
            check_marks += "✔"
            mark_label.config(text=check_marks)

# ---------------------------- GUI ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 30, 'bold'), fill='white')
canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset)
reset_button.grid(column=2, row=2)

mark_label = Label(text="", font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)
mark_label.grid(column=1, row=3)

window.mainloop()