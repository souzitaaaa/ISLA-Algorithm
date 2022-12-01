import random

def guess(x):
    random_nmr = random.randint(1,x)
    guess = 0
    while guess != random_nmr:
        guess = int(input('Guess a number between 1 and {}: '.format(x)))
        #guess = int(input(f'Guess a number between 1 and {}: '))
        if guess < random_nmr:
            print("Try again, too low!")
        if guess > random_nmr:
            print("Try again, too high")
    print("Congratulations, you guesses the number righ!")

guess(20)
