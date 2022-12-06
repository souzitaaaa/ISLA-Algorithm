import random

min_val = 1
max_val = 6

roll = input("Do you want to roll de dices?\n")
while roll == "yes" or roll == "Yes" or roll == "y":
    print("Dices rolling...")
    print("You got: ")
    print (random.randint(min_val, max_val))
    roll = input("Roll again?\n")