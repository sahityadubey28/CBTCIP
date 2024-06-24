import random

def generate_secret_number(digits):
    return ''.join(random.sample('0123456789', digits))

def get_feedback(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def player_set_number(player_name, digits):
    while True:
        number = input(f"{player_name}, set your {digits}-digit number: ")
        if len(number) == digits and number.isdigit() and len(set(number)) == digits:
            return number
        print(f"Please enter a valid {digits}-digit number with unique digits.")

def player_guess_number(player_name, digits):
    guess = input(f"{player_name}, enter your guess ({digits} digits): ")
    return guess

def play_round(setting_player, guessing_player, digits):
    print(f"\n{setting_player}'s turn to set the number.")
    secret_number = player_set_number(setting_player, digits)
    print("\n" * 100)  # Clear the screen (works in most terminals)

    attempts = 0
    while True:
        attempts += 1
        guess = player_guess_number(guessing_player, digits)
        bulls, cows = get_feedback(secret_number, guess)

        if bulls == digits:
            print(f"Congratulations! {guessing_player} guessed the number in {attempts} attempts.")
            return attempts

        print(f"Bulls: {bulls}, Cows: {cows}")

def main():
    print("Welcome to the Mastermind Game!")
    digits = 4  # You can change this to increase/decrease difficulty

    player1_attempts = play_round("Player 1", "Player 2", digits)

    if player1_attempts == 1:
        print("Player 2 is crowned Mastermind for guessing in the first attempt!")
        return

    player2_attempts = play_round("Player 2", "Player 1", digits)

    if player1_attempts < player2_attempts:
        print("Player 1 wins and is crowned Mastermind!")
    else:
        print("Player 2 wins and is crowned Mastermind!")

if __name__ == "__main__":
    main()