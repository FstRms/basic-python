""" Script to verify if a certain year was a leap year. """
import datetime as dt

print("Hi there!!!\nWelcome to the Leap Year Verify tool!!!\n")
year = int(input("Please enter the year you want to verify:\n"))
verb = None

check_today = dt.datetime.now()
current_year = check_today.year
if year < current_year:
    verb = "was"
else:
    verb = "is"

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} {verb} a Leap Year")
        else:
            print(f"The year {year} {verb} not a Leap Year")
    else:
        print(f"The year {year} {verb} a Leap Year")
else:
    print(f"The year {year} {verb} not a Leap Year")
