"""A number-guessing game."""

# Put your code here
import random

print("Howdy, what's your name?")

# input the name and save it to a variable
name = input("Type in your name: ")

# we need to generate a random number between 1 and 100
number = random.randint(1,100)
