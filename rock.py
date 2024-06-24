import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()