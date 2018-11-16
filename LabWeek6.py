# Sean Brooks
# x00152000

# A program to calculate a person's age to see if they are eligible for a driver's license.

import time
PROVISIONAL_AGE = 17

# Get input
age = str(input("Input age in format DD/MM/YYYY : "))

# Variables
dayInput = int(age[0:2])
monthInput = int(age[3:5])
yearInput = int(age[6:10])
dayCompare = int(time.strftime("%d"))
monthCompare = int(time.strftime("%m"))
yearCompare = int(time.strftime("%Y"))

# Calculate and Display
if yearInput < yearCompare - PROVISIONAL_AGE:
    print("You are old enough for a provisional license. Y")
elif monthInput < monthCompare:
    print("You are old enough for a provisional license. M")
elif dayInput <= dayCompare:
    print("You are old enough for a provisional license. D")
else:
    print("You are not old enough. X")
