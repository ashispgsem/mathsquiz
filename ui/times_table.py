import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import random
import time

class QuizApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.reset_quiz()


  
    def create_widgets(self):
        for i in range (self.total_questions):
            num1 = random.randint(12, 15)
            num2 = random.randint(2,12)
            answer = num1*num2
            self.real_answers.append(answer)
            # grid method to arrange labels in respective
            # rows and columns as specified
            l1 = tk.Label(self, text = f"What is {num1} X {num2}: ")
            l1.grid(row = i, column = 0)
            l2 = tk.Label(self, text = "                                    ")
            l2.grid(row = i, column = 3)
            self.entry_answer.append(Entry(self))
            self.entry_answer[i].delete(0, "end")
            self.entry_answer[i].grid(row = i, column = 1)
            
        b = tk.Button(self, text = "Submit", command=self.check_answer)
        b.grid(row = i+1, column=2)

        b = tk.Button(self, text = "Close", command=self.close_app)
        b.grid(row = i+1, column=1)


    def check_answer(self):
        for i in range (self.total_questions):
            user_answer = int(self.entry_answer[i].get())
            if  user_answer == self.real_answers[i]:
                self.score += 1
            
            l2 = tk.Label(self, text = f"Correct Answer is {self.real_answers[i]} ")
            l2.grid(row = i, column = 3)
        total_time = time.time() - self.start_time
        messagebox.showinfo(title = "Info", message = f"Quiz Score. Congratulations, You have completed the quiz! \n \
                        Your score is {self.score} out of {self.total_questions}. \nYou took {int(total_time)} seconds ")

        b2 = tk.Button(self, text = "Reset", command=self.reset_quiz)
        b2.grid(row = i+1, column=3)

    def reset_quiz(self):
        self.real_answers = []
        self.user_answers =[]
        self.score = 0
        self.entry_answer = []
        self.total_questions = 10
        self.create_widgets()
        self.start_time = time.time()

    def close_app(self):
        self.destroy()
   
app = QuizApp()
app.mainloop()
