# Task 1
questions = [
    "What is the tallest mountain?",
    "How many tentacles does an octopus have?",
    "What is the national animal of Scotland?",
]

correct_answers = ["Mount Everest", "8", "Unicorn"]
guesses = []

score = 0

for i in range(len(questions)):
    guess = input(questions[i] + " ")
    guesses.append(guess)
    try:
        if guess == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
    except ValueError:
        print("Invalid input")
print(f"Your score is {score}/{len(questions)}.")

if score == 0:
    print("You didn't get any correct. Try again.")
elif score == 1:
    print("Study and try agin.")
elif score == 2:
    print("More than half correct!")
else:
    print("You got them all correct!")