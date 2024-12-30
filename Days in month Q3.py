month = int(input("Enter a month in 2024(1-12): "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("The number of days in",month,"month in 2024 is 31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("The number of days in",month,"month in 2024 is 30 days")
elif month == 2:
    print("The number of days in",month,"month in 2024 is 30 days")
else:
    print("Invalid month. Please enter a number between 1 and 12.")