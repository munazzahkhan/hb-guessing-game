"""A number-guessing game."""

# Put your code here
import random

print("Howdy, what's your name?")

# input the name and save it to a variable
name = input("Type in your name: ")
print("I am thinking of a number between 1 and 100")

def prompt_to_play_again():
    """ keep asking the player to enter a valid yes/no response """

    play_again = input("Do you wish to play again (yes/no)? ")
    while play_again.lower() != "yes" and play_again.lower() != "no":
        play_again = input("Please only enter yes/no: ")
    return play_again

best_score = 0

while True:

    count = 1
    # we need to generate a random number between 1 and 100
    number = random.randint(1,100)

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
    
    # update best_score to the lowest number of tries in any game
    if best_score == 0:
        best_score = count
    elif best_score > count:
        best_score = count
    
    # if player response is "yes" then continue otherwise end the game with a message
    response = prompt_to_play_again()
    if response == "yes":
        continue
    elif response == "no":
        print(f"Thanks for playing. Your best guess was in {best_score} tries")
        break        