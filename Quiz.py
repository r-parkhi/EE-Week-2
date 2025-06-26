# --- Imports ---
import random;
import time;


# --- Main Program ---

# Question & answer list
questions = [
    {"prompt": "What year was the Declaration of Independence signed?\n", "answer": "1776"},
    {"prompt": "In what mountain range is Mount Everest located?\n", "answer": "The Himalayas"},
    {"prompt": "Who wrote the novel \033[3mTo Kill a Mockingbird?\033[0m\n", "answer": "Harper Lee"},
    {"prompt": "What is the most plentiful gas on Earth?\n", "answer": "nitrogen"},
    {"prompt": "What was the name of the Nazi cipher device broken by Alan Turing?.\n", "answer": "the Enigma"},
]

# Shuffle question order
random.shuffle(questions);

# Loop through each question
score = 0
for q in questions:
    # Ask the user the question
    user_input = input(q["prompt"] + "Your answer: ").strip().lower()

    # Check for blank input
    while user_input.strip() == "":
        user_input = input(q["prompt"] + "Your answer: ").strip().lower()

    # Mark answer correct/incorrect
    answerForm = q["answer"].lower();
    if user_input == answerForm:
        print("\033[32mCorrect\033[0m.\n");
        score += 1;
    else:
        print(f"\033[31mIncorrect\033[0m. The correct answer was {q["answer"]}.\n");


# Display final score & percentage
percentage = round(100 * (score / len(questions)));

print("Your score is");
for i in range (3):
    print(".");
    time.sleep(0.5);
print(f"a {score} out of {len(questions)}! That means you got {percentage}% correct.");