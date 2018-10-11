# Sean Brooks
# x00152000

# A program to check if two numbers divide cleanly.

# Gather data from user
numberOne = float(input("Input the first number: "))
numberTwo = float(input("Input the second number: "))

# Modulus divide the two numbers
result = (numberTwo % numberOne)
if result == 0:
    print("Successful clean division")
else:
    print("Failed clean division")

#################################################################

# A program to indicate purchase policies

# Gather data from user
cost = float(input("Input item cost: € "))

# Process data through company policy and display response
if cost > 10000:
    print("You must go to tender to request purchase of this item")
elif cost > 500:
    print("You must get three price quotes for the item and purchase the cheapest")
elif cost > 0:
    print("You may purchase the item")
else:
    print("Price cannot be zero or less, please try again")

#################################################################

# A program to display a student's grade

# Grade requirement lower limits:
GRADE_A = 80
GRADE_BP = 70
GRADE_B = 60
GRADE_BM = 55
GRADE_CP = 50
GRADE_C = 40
GRADE_D = 35
GRADE_F = 0

# Receive data as a percentage
grade = float(input("Input grade as a % "))

# Pass grade input through grade requirement limits.
if grade >= GRADE_A:
    print("A")
elif grade >= GRADE_BP:
    print("B+")
elif grade >= GRADE_B:
    print("B")
elif grade >= GRADE_BM:
    print("B-")
elif grade >= GRADE_CP:
    print("C+")
elif grade >= GRADE_C:
    print("C")
elif grade >= GRADE_D:
    print("D")
else:
    print("F")

#################################################################

# Random Password Checker

import random

password = input("Input a password: ")

PASS_LENGTH = len(password)

# First Number
numberOne = (random.randint(0, PASS_LENGTH-1))
passwordOne = str(password[numberOne])

# Second Number
numberTwo = (random.randint(0, PASS_LENGTH-1))
passwordTwo = str(password[numberTwo])

# Third Number
numberThree = (random.randint(0, PASS_LENGTH-1))
passwordThree = str(password[numberThree])

# Request Characters
print("Input Character", numberOne+1)
checkOne = str(input(""))
print("Input Character", numberTwo+1)
checkTwo = str(input(""))
print("Input Character", numberThree+1)
checkThree = str(input(""))

# Check all characters
if checkOne == passwordOne:
    if checkTwo == passwordTwo:
        if checkThree == passwordThree:
             print("Success")
else:
    print("Fail")