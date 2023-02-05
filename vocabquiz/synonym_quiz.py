import csv
import random

def load_synonyms(filename):
    synonyms = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            word = row[0]
            options = row[1:]
            synonyms[word] = options
    return synonyms

print("\n\n**********Starting Synonym Quiz*****************\n")
level = input("Please select a difficulty level - 1 (easy) or 2 (difficult)\n")
if level == 1:
    filename = "easysyn.csv"
else:
    filename = "diffsyn.csv" 
synonyms = load_synonyms(filename)

score = 0

for word, options in synonyms.items():  
    options = options.copy()
    correct_answer = options[0]
    # options.append(correct_answer)
    random.shuffle(options)

    print(f"What is a synonym of {word}?")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    user_answer = input("Enter the number of your answer: ")
    user_answer = options[int(user_answer) - 1]

    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The synonym of {word} is {correct_answer}.")

print(f"You scored {score} out of {len(synonyms)}.")
