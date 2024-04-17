import Difficulty

# Choosing the difficulty

print("Welcome to Rock, Paper, Scissors tournament. Choose your difficulty level:")

bot_difficulty = Difficulty.bot_hard

diff_answer = ""

while diff_answer not in ['a', 'b', 'c']:
    diff_answer = input("(a) Easy\n(b) Hard\n(c) Impossible\n\n")
    if diff_answer == "a":
        bot_difficulty = Difficulty.bot_easy
    elif diff_answer == "b":
        bot_difficulty = Difficulty.bot_hard
    elif diff_answer == "c":
        bot_difficulty = Difficulty.bot_impossible
    else:
        print("Try again!")

# Tournament

my_score = 0
bot_score = 0
my_choice = ""
bot_choice = ""

options = ["rock", "paper", "scissors"]

print("Let's start!\nChoose rock, paper or scissors:\n")

while my_score != 3 and bot_score != 3:
    my_choice = input("Rock, paper, scissors! ")
    if my_choice in options:
        bot_choice = bot_difficulty(my_choice)
        print("\nBot chose: " + bot_choice)
        if my_choice == "rock" and bot_choice == "scissors":
            print("You win!")
            my_score += 1
        elif my_choice == "paper" and bot_choice == "rock":
            print("You win!")
            my_score += 1
        elif my_choice == "scissors" and bot_choice == "paper":
            print("You win!")
            my_score += 1
        elif my_choice == bot_choice:
            print("Draw!")
        else:
            print("Bot wins!")
            bot_score += 1
    else:
        print("Miss-click!")
    print("You: " + str(my_score) + ":" + str(bot_score) + " Bot\n")

if my_score == 3:
    print("YOU ARE THE WINNER!")
else:
    print("BOT IS THE WINNER!")
