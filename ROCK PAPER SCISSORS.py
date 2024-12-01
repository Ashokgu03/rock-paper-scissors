import random

# Function to get the computer's choice
def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Options: rock, paper, or scissors")

        # User input
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please select either rock, paper, or scissors.")
            continue

        # Computer makes a choice
        comp_choice = computer_choice()
        print(f"Computer chose: {comp_choice}")

        result = determine_winner(user_choice, comp_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display scores
        print(f"Your Score: {user_score} | Computer Score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()