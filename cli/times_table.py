import random
import time

num_questions = 10
min_num = 12
max_num = 15
time_limit = 45
time_taken = 0

start_time = time.time()
print("\n\n********************Let us start the game**************************")

score = 0
for i in range(num_questions):
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(2, 12)
    answer = num1 * num2

    if time_taken > time_limit:
        break
    user_answer = int(input(f"What is {num1} * {num2}? "))
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
    time_taken = time.time() - start_time
    print (f"Remaining Time: {int(time_limit-time_taken)} \n")
total_time = (time.time() - start_time)

print(f"   You scored {score}/{num_questions}.")
print(f"\n   You have taken {int(total_time)} seconds. \n  Let us improve it even further next time!")
print("\n\n********************Game Over**************************")