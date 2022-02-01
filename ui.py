import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_IMG = r"images/true.png"
FALSE_IMG = r"images/false.png"
FONT_LABEL = ("Arial", 15, "italic")
FONT_CANVAS = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = tkinter.Label(text="Score:", fg="white", bg=THEME_COLOR, font=FONT_LABEL)
        self.label.grid(column=1, row=0)

        t_img = tkinter.PhotoImage(file=TRUE_IMG)
        self.true_button = tkinter.Button(image=t_img,
                                          highlightthickness=0,
                                          bg=THEME_COLOR,
                                          command=self.answer_true)
        self.true_button.grid(column=0, row=2)
        f_img = tkinter.PhotoImage(file=FALSE_IMG)
        self.false_button = tkinter.Button(image=f_img,
                                           highlightthickness=0,
                                           bg=THEME_COLOR,
                                           command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.text_canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.text_canvas.create_text(150,
                                                          125,
                                                          text="Some text.",
                                                          fill=THEME_COLOR,
                                                          font=FONT_CANVAS,
                                                          width=280)
        self.text_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.text_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.text_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.text_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right):
        if is_right:
            self.text_canvas.config(bg="green")
        else:
            self.text_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
