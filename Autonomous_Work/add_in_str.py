def add_is(string):
    if len(string) >= 2 and string[:2] == "Is":
        return string
    return "Is" + string

string = input("Write something: ")
print(add_is(string))
