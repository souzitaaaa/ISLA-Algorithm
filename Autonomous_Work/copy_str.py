def copy_str(string, n):
    result = ""
    for i in range(n):
        result = result + string
    return result


string = input("Write something: ")
n = int(input("How many times do you want to multiplicate? "))
print(copy_str(string, n))