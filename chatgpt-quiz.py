import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self, questions, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.questions = questions
        self.current_question = 0
        self.create_widgets()

    def create_widgets(self):
        self.label_question = tk.Label(self, text=self.questions[self.current_question][0])
        self.label_question.pack()

        self.entry_answer = tk.Entry(self)
        self.entry_answer.pack()

        self.button_submit = tk.Button(self, text="Submit", command=self.check_answer)
        self.button_submit.pack()

    def check_answer(self):
        if self.entry_answer.get().lower() == self.questions[self.current_question][1].lower():
            self.current_question += 1
            if self.current_question == len(self.questions):
                messagebox.showinfo("Quiz", "You completed the quiz!")
                self.destroy()
            else:
                self.label_question.config(text=self.questions[self.current_question][0])
                self.entry_answer.delete(0, tk.END)
        else:
            messagebox.showerror("Quiz", "Incorrect answer, try again")

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is the capital of Italy?", "Rome")
]

app = QuizApp(questions)
app.mainloop()
