import random
import time

num_questions = 5
min_num = 201
max_num = 999
time_limit = 45
time_taken = 0


number1 =[]
number2 = []
real_answers = []
user_answers =[]

start_time = time.time()
print(f"Start time is {start_time}")
score = 0
for i in range(num_questions):
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(22, 99)
    answer = num1 * num2
    number1.append(num1)
    number2.append(num2)
    real_answers.append(answer)


    time_taken = time.time() - start_time
    if time_taken > time_limit:
        break
    user_answer = int(input(f"What is {num1} * {num2}? "))
    
    user_answers.append(user_answer)

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
    print (f"Remaining Time: {time_limit-time_taken}")
total_time = (time.time() - start_time)
print(f"You scored {score}/{num_questions}.")
print(f"You have taken {total_time}. Could you try improving next time!")

print("See How did it\n")
print("NUMBER1 NUMBER2 RIGHT_ANSWER UR_ANSWER \n")

for i in range(num_questions):
    print(f"{number1[i]}   X   {number2[i]}  =    {real_answers[i]}      {user_answers[i]}")

