import calendar

year = int(input("Insert the year: "))
month = int(input("Insert which month you want to see: "))

print()
print(calendar.month(year,month))

print("Now printing the calendar of 2023")
print()

month = 1
while  month in range (13):
    print(calendar.month(2023, month))
    month += 1