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
    guess = input("Guess the number >  ")
    try:
        int(guess)
        if int(guess) < 1 or int(guess) > 100:
            print("Please only pick a number between 1 and 100.")
            count += 1
        elif int(guess) < number:
            print("Your guess is too low, try again.")
            count += 1
        elif int(guess) > number:
            print("Your guess is too high, try again.")
            count += 1
        else:
            print("You are correct.")
            print(f"You guessed in {count} tries.")
            break
    except:
            print("Please only enter an integer.")
            count += 1
    



