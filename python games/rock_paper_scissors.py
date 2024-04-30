import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if player_choice == "quit":
            print("Thanks for playing!")
            break

        computer_choice = random.choice(choices)

        print(f"You chose {player_choice}, and the computer chose {computer_choice}.")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

rock_paper_scissors()
