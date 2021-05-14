""" Basic Script to calculate tip"""

print("Hi there!!!\nWelcome to the Tip Calculator tool!!!\n")
bill = float(input("How much was the total bill?\n"))
tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")  
people = int(input("How many people to split the bill?\n"))

tip_fix = float("1."+tip)
split = round((bill * tip_fix) / people,2)
print (f"Each person should pay {split}") 