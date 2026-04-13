import random
from random import randint

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

counter = 0
number = randint(1, 100)

if difficulty == "easy":    counter += 10
if difficulty == "hard":    counter += 5


while counter > 0:
    print(f"You have {counter} guesses left")
    current_guess = int(input("Make a guess: "))
    if current_guess == number:
        print(" --- !!! YOU WON !!! ---")
        break
    else:
        if current_guess > number:
            counter -= 1
            print("Too high!")
        else:
            counter -= 1
            print("Too low!")

    if counter == 0:    print("You lost... Game over.")