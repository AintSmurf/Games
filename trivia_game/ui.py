import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UI:
    def __init__(self, quizbrain: QuizBrain):
        self.tracker = 0
        self.ls_for_user = []
        self.quiz = quizbrain
        self.window = tk.Tk()
        self.window.title("Trivia Game")
        self.window.resizable(0, 0)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = tk.Label(
            text=f"score: {self.tracker}",
            bg=THEME_COLOR,
            fg="white",
            font=("Ariel", 18, "italic"),
        )
        self.score.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=600, height=400)
        self.questiontext = self.canvas.create_text(
            300,
            200,
            width=450,
            text="",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"),
        )

        # texts for the answers
        self.answer1 = self.canvas.create_text(
            220,
            320,
            width=450,
            text="",
            fill=THEME_COLOR,
            font=("Ariel", 12, "italic"),
        )
        self.answer2 = self.canvas.create_text(
            220,
            340,
            width=450,
            text="",
            fill=THEME_COLOR,
            font=("Ariel", 12, "italic"),
        )
        self.answer3 = self.canvas.create_text(
            440,
            320,
            width=450,
            text="",
            fill=THEME_COLOR,
            font=("Ariel", 12, "italic"),
        )
        self.answer4 = self.canvas.create_text(
            440,
            340,
            width=450,
            text="",
            fill=THEME_COLOR,
            font=("Ariel", 12, "italic"),
        )
        # b1 = tk.Button(self.canvas, text="testomg", bg="red")
        # self.canvas.create_window(300, 200, window=b1)

        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)

        r = tk.PhotoImage(file="images/true.png")
        f = tk.PhotoImage(file="images/false.png")

        self.explain = tk.Label(
            text="",
            bg=THEME_COLOR,
            fg="white",
            font=("Ariel", 12, "italic"),
        )
        self.explain.grid(row=2, column=1)

        self.right = tk.Button(image=r, highlightthickness=0, command=self.true_answer)
        self.right.grid(row=3, column=0)
        self.answer = tk.Entry(width=25, font=("italic 14"), fg="green")
        self.answer.bind("<Return>", self.get_user_input)
        self.answer.grid(row=3, column=1)
        self.wrong = tk.Button(image=f, highlightthickness=0, command=self.false_answer)
        self.wrong.grid(row=3, column=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"score: {self.tracker}")
            q_text = self.quiz.next_question()
            self.ls_for_user = self.quiz.ls_for_user
            type = self.quiz.get_type()

            if type == "boolean":
                self.explain.config(text="")
                self.activate_buttons()
            else:
                self.explain.config(text="Pick A number:")
                self.canvas.itemconfig(
                    self.answer1,
                    text=f"1. { self.ls_for_user [0]}",
                    anchor=tk.CENTER,
                )
                self.canvas.itemconfig(
                    self.answer2,
                    text=f"2. { self.ls_for_user [1]}",
                    anchor=tk.CENTER,
                )
                self.canvas.itemconfig(
                    self.answer3,
                    text=f"3. { self.ls_for_user [2]}",
                    anchor=tk.CENTER,
                )
                self.canvas.itemconfig(
                    self.answer4,
                    text=f"4. { self.ls_for_user [3]}",
                    anchor=tk.CENTER,
                )
                self.disable_buttons()

            self.canvas.itemconfig(self.questiontext, text=q_text)
        else:
            quit()

    def get_user_input(self, event):
        number = self.answer.get()
        if number == 1:
            answer = self.ls_for_user[0]
        elif number == 2:
            answer = self.ls_for_user[1]
        elif number == 3:
            answer = self.ls_for_user[2]
        else:
            answer = self.ls_for_user[3]
        self.give_feed_back(self.quiz.check_answer(answer))
        self.answer.delete(0, tk.END)

    def disable_buttons(self):
        self.right.config(state="disabled")
        self.wrong.config(state="disabled")
        self.answer.config(state="normal", background=THEME_COLOR)

    def activate_buttons(self):
        self.right.config(state="active")
        self.wrong.config(state="active")
        self.answer.config(state="disabled")

    def true_answer(self):
        self.give_feed_back(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feed_back(self.quiz.check_answer("False"))

    def give_feed_back(self, isright):
        if isright == True:
            self.canvas.config(bg="green")
            self.tracker += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)


# print(self.canvas.itemcget(self.questiontext, "text"))
