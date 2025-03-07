# Guess the number
import random

n = random.randint(
    1, 10
)  # function generates the random number between the given ranges

guess = 0

while guess != n:
    guess = int(input("Enter the number: "))

    if guess < n:
        print("Your guess is smaller")

    elif guess > n:
        print("Your guess is greater")

    else:
        print("You guessed the correct number")
