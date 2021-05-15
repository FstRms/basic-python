""" Script to verify if a certain year was a leap year. """

print("Hi there!!!\nWelcome to the Leap Year Verify tool!!!\n")
year = int(input("Please enter the year you want to verify:\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a Leap Year")
        else:
            print(f"The year {year} is not a Leap Year")
    else:
        print(f"The year {year} is a Leap Year")
else:
    print(f"The year {year} is not a Leap Year")
