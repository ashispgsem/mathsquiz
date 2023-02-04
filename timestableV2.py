import random
import time
import tkinter as tk
from tkinter import messagebox

# def start_quiz():
#     global name
#     name = question_entry.get()

#     question_entry.pack_forget()
#     start_button.pack_forget()
#     question_label["text"] = f"{name}: Quiz is starting now!"

#     answer_button = tk.Button(window, text="Answer", font=("TkDefaultFont", 14), command=show_questions)
#     answer_button.pack()
   
    

def start_quiz():
    global score
    score = 0

    global name
    name = question_entry.get()

    # Hiding Start Quiz Button permanently 
    start_button.pack_forget()

    # Hiding Text box till Quiz Starts
    question_entry.delete(0, "end")
    question_entry.pack_forget()
    
    question_label["text"] = f"{name}: Quiz is starting now!"

    # Unhider Answer Button
    answer_button.pack()

    num_questions = 10
    time_limit = 45
    time_taken = 0
    time_remaining = time_limit - time_taken
    start_time = time.time()
    question_label["text"] = f"Name: {name}, NumQ:{num_questions}, timelimit: {time_limit}, timeremaining: {time_remaining}" 

    for i in range(num_questions):

def calculate_score_time(): 
    score = score


  
def show_questions():  
    min_num = 12
    max_num = 15
    
    
    for i in range(num_questions):
        question_label["text"] = f"{name}: {i}"
     
        # num1 = random.randint(min_num, max_num)
        # num2 = random.randint(2,12)
        # answer = num1 * num2
   
        # question_label["text"] = f"{name}: your Score is {score}/{i}. \n Total time remaining is {time_remaining}. \nWhat is {num1} * {num2}?"
        # if i < 2:
        #     question_entry.pack()
        #     answer_button["text"] = "Answer"

        # # Calculate Time
        # time_taken = time.time() - start_time
        # time_remaining = 45-time_taken
        # if time_taken > time_limit:
        #     break
        # user_answer = int(question_entry.get())
        # if user_answer == answer:
        #     score += 1
        # # Show Question Label
        # question_entry.delete(0, "end")

    # end_time = time.time()
    # total_time = end_time - start_time
    messagebox.showinfo("Quiz Completed", f"You scored {score}/{num_questions}. You have taken {time_taken} seconds")

window = tk.Tk()
window.title("Multiplication Quiz")

question_label = tk.Label(window, text="Welcome to the Multiplication Quiz!, \nEnter your name below", font=("TkDefaultFont", 14))
question_label.pack()

question_entry = tk.Entry(window, font=("TkDefaultFont", 14))
question_entry.pack()

start_button = tk.Button(window, text="Start Quiz", font=("TkDefaultFont", 14), command=start_quiz)
start_button.pack()

answer_button = tk.Button(window, text="OK", font=("TkDefaultFont", 14), command=calculate_score_time)

window.mainloop()
