from random import randint


def bot_easy(choice):
    if choice == "scissors":
        return "paper"
    elif choice == "paper":
        return "rock"
    elif choice == "rock":
        return "scissors"
    else:
        return "nothing"


def bot_hard(choice):
    options = ["rock", "paper", "scissors"]
    return options[randint(0, 2)]


def bot_impossible(choice):
    if choice == "scissors":
        return "rock"
    elif choice == "paper":
        return "scissors"
    elif choice == "rock":
        return "paper"
    else:
        return "nothing"

