""" Script to verify if a number is a prime number. """

def prime_checker(number):
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime = False
    if prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

print("Hi there!!!\nWelcome to Prime Number Checker!!!\n")

n = int(input("Check this number: "))
prime_checker(number=n)
