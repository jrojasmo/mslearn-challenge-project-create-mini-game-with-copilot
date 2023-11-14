# APP to make a full rock paper scissors game on terminal
# Animation of the welcome message and display of the rules
import time

welcome_message = "Welcome to the Rock Paper Scissors game! \n Here are the rules: \n Rock beats scissors \n Scissors beats paper \n Paper beats rock \n To quit the game, enter 'q'"
for char in welcome_message:
    print(char, end='', flush=True)
    time.sleep(0.05)  # adjust the speed of the animation by changing this value
print()  # print a newline character at the end

# import random module
import random
# create a list of options
options = ["rock", "paper", "scissors"]
# create a variable to store the computer's choice
computer_choice = random.choice(options)
# create a variable to store the result
result = ""
user_choice = ""
# add a counter to keep track of the score and number of games played
counter = 0
score = 0
# create a while loop to check if the user wants to quit
while True:
    # store the user's choice
    user_choice = input("Enter your choice: ")
    user_choice = user_choice.lower()
    # check if the user wants to quit
    if user_choice == "q":
        print("Bye!")
        # print the score and number of games played
        print("You played " + str(counter) + " games and won " + str(score) + " games.")
        break
    # check if the user's choice is valid
    if user_choice not in options:
        print("Invalid choice. Try again.")
        continue
    # store the computer's choice
    computer_choice = random.choice(options)
    # check if the user's choice is the same as the computer's choice
    if user_choice == computer_choice:
        result = "It's a tie!"
    # check if the user won
    elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "rock":
        result = "You won!"
        score += 1
    else:
        result = "You lost!"
    # print the result
    counter += 1
    print("You chose " + user_choice + ". The computer chose " + computer_choice + ". " + result)
    

    