from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, pady=25)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            width=200,
            text='',
            fill=THEME_COLOR,
            font=("Arial", 12, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_button)
        self.true_button.grid(column=0, row=2, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_button)
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')



