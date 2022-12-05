def addition():

    print("\n")
    print("Addition\n")
    n = float(input("Enter a number: "))
    Calcs = n
    while (n != 0):
        n = float(input("Enter a number to add: "))
        Calcs += n
    return (Calcs)

def subtraction():

    print("\n")
    print("Subtraction\n")
    n = float(input("Enter a number: "))
    Calcs = n
    while (n != 0):
        n = float(input("Enter a number to subtract: "))
        Calcs -= n
    return (Calcs)

def multiplication():

    print("\n")
    print("Multiplicaton\n")
    n = float(input("Enter a number: "))
    Calcs = 1
    while (n != 0):
        Calcs *= n
        n = float(input("Enter a number to multiply: "))
    return (Calcs)

def division():

    print("\n")
    print("Divison\n")
    n = float(input("Enter a number: "))
    Calcs = n
    while (n != 0):
        n = float(input("Enter a number to divide: "))
        Calcs =  Calcs/n
        loop = input("Do you want to keep dividing?\n")
        if loop == "no" or loop == "No" or loop == "n":
            break
    return (Calcs)

print ("\n")
print ("Calculator\n")
print ("Enter 'a' for addition")
print ("Enter 's' for subtraction")
print ("Enter 'm' for multiplication")
print ("Enter 'd' for division")
print ("Enter 'q' to quit\n")
Operation = input("What do you want to do: ")

if Operation != 'q':

    if Operation == 'a':
        Result = addition()
        print ("Answer =", Result)
    if Operation == 's':
        Result = subtraction()
        print ("Answer =", Result)
    if Operation == 'm':
        Result = multiplication()
        print ("Answer =", Result)
    if Operation == 'd':
        Result = division()
        print ("Answer =", Result)
    

