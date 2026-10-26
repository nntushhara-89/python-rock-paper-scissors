
import random


def play_game():
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    user = input("Choose rock, paper, or scissors: ").strip().lower()

    if user not in choices:
        print("Invalid choice! Please try again.")
        return

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    play_game()
