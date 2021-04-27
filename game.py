"""A number-guessing game."""

# Put your code here
import random

print("Howdy, what's your name?")

# input the name and save it to a variable
name = input("Type in your name: ")
print("I am thinking of a number between 1 and 100")

# we need to generate a random number between 1 and 100
number = random.randint(1,100)

count = 0

# loop till the number is equal to the guess
while True:
    #prompt the player to guess the number
    guess = int(input("Guess the number >  "))
    if guess < number:
        print("Your guess is too low, try again.")
        count += 1
    elif guess > number:
        print("Your guess is too high, try again.")
        count += 1
    else:
        print("You are correct.")
        print(f"You guessed in {count} tries.")
        break
    



