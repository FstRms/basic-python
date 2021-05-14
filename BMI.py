""" Script to calculate Body Mass Index"""

print("Hi there!!!\nWelcome to the Body Mass Index Calculator tool!!!\n")
height = float(input("Please enter your height in m:\n"))
weight = float(input("Please enter your weight in kg:\n"))
bmi = int(weight / (height ** 2))

if bmi < 18.5:
    print (f"Your BMI is {bmi}. You are Underweight")
elif bmi < 25:
    print (f"Your BMI is {bmi}. You have Normal weight")
elif bmi < 30:
    print (f"Your BMI is {bmi}. You have Overweight")
elif bmi < 35:
    print (f"Your BMI is {bmi}. You have Obesity")
else:
    print("Your BMI is {bmi}. You have Clinnical Obesity")