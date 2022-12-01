import random

def game():
    user = input("'r' for rock, 'p' for paper and 's' for scissor\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return("It's a tie!")
    if win(user, computer):
        return("You won!")
    return("You lost!")

def win(user, computer):

    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True

print(game())
