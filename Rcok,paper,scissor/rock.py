import random  # Importing the random module to generate computer's choice

def play_game():
    # List of choices for the game
    choices = ['rock', 'paper', 'scissors']
    # Randomly choosing computer's choice from the list
    computer_choice = random.choice(choices)
    # Getting user's choice and converting it to lowercase
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    # Printing computer's choice
    print(f"Computer chose: {computer_choice}")

    
    if user_choice not in choices:
        print("Invalid choice. Please choose again.")
        play_game()  # Asking user to choose again if choice is invalid
    
    elif user_choice == computer_choice:
        print("It's a tie!")
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    
    else:
        print("You lose!")

    # Asking user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()  # If user wants to play again, calling play_game() function recursively
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()  # Starting the game when the script is executed
