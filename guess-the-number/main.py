from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while difficulty not in ["easy", "hard"]:
    print("Invalid input. Please choose 'easy' or 'hard'.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempt_remaining = 0
if difficulty == "hard":
    attempt_remaining = 5
elif difficulty == "easy":
    attempt_remaining = 10

zero_attempt = False
random_number = random.randint(1, 100)
correct_guess = False

while not zero_attempt:
    print(f"You have {attempt_remaining} attempts remaining to guess the number")

    try:
        user_guess = int(input("Make a guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if user_guess < 1 or user_guess > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    if user_guess == random_number:
        print(f"You got it! The answer was {random_number}")
        correct_guess = True
        break
    elif user_guess > random_number:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")

    attempt_remaining -= 1
    if attempt_remaining == 0:
        print(f"You've run out of guesses, you lose. The answer was {random_number}.")
        break

if correct_guess:
    print(f"Congratulations, you won!")
