# Project Rock, Paper Scissors by Nicholas Caro
# Start Date: October, 2nd 2022
# Finish Date: October, 2nd 2022

from random import randint
from time import sleep

# Need a selection for object by the user directly and the computer
userSelection = input("Please choose either Rock or Paper or Scissors: ")
computerSelection = randint(0,2) # Rock = 0, Paper = 1 and Scissors = 2

# Ensures that the user inputted a calculable value
if userSelection == "Rock" or userSelection == "Paper" or userSelection == "Scissors":
    sleep(1.5)
    print(f"You selected {userSelection}")
else:
    sleep(1.5)
    print("Please re-run the program and choose either Rock or Paper or Scissors.")

# Tells the user what the computer selected
if computerSelection == 0:
    sleep(1.5)
    print("Computer selects Rock")
elif computerSelection == 1:
    sleep(1.5)
    print("Computer selects Paper")
else:
    sleep(1.5)
    print("Computer selects Scissors")

def game():
    sleep(1.5)
    if userSelection == "Rock":
        if computerSelection == 0: # Rock and Rock
            print("Tie! Both you and the computer chose Rock")
        elif computerSelection == 1: # Rock and Paper
            print("Loss! Your Rock got covered by the computer's Rock")
        else: # Rock and Scissors
            print("Win! Your Rock crushed the computer's Scissors")
    
    if userSelection == "Paper":
        if computerSelection == 0: # Paper and Rock
            print("Win! Your Paper covered the computer's Rock")
        elif computerSelection == 1: # Paper and Paper
            print("Tie! Both you and the computer chose Paper")
        else: # Paper and Scissors
            print("Lose! Your Paper got cut by the computer's Scissors")
    
    if userSelection == "Scissors":
        if computerSelection == 0: # Scissors and Rock
            print("Lose! Your Scissors got crushed by the computer's Rock")
        elif computerSelection == 1: # Scissors and Paper
            print("Win! Your paper cut the computer's Paper")
        else: # Scissors and Scissors
            print("Tie! Both you and the computer chose Scissors")
game()
