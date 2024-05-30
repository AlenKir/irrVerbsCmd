import csv
import random

from verb import IrregularVerb

heart_sign = "\U00002764"
skull_sign = "\U0001F480"

verbs = []

with open('../data/verbs.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')

    for v in csv_reader:
        verb = IrregularVerb(v[0], v[1], v[2], v[3])
        verbs.append(verb)

while True:
    try:
        level = int(input("How many forms do you want to guess?\n"))
        if 1 <= level <= 3:
            print(f"You will have to guess {level} forms.")
            break
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

while verbs:
    index = random.randrange(len(verbs))
    guess_verb = verbs[index]
    task, solution = guess_verb.get_task(hide_forms=level)
    print(task)
    user_guess = input("Enter the missing form:\n")
    if user_guess == solution:
        verbs.pop(index)
        print(f"Correct! {heart_sign}")
    else:
        verbs.append(guess_verb)
        print(f"Wrong! {skull_sign}")
        print("Correct:", solution)
        input("Type out the answer again to remember:\n")
    print("")

print("THE END.")
