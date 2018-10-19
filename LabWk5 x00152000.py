# Sean Brooks
# x 00152000

# Blackjack, kinda

import random

# Create cards
cpuCard = random.randint(1, 20)
plyCard1 = random.randint(1, 20)
plyCard2 = random.randint(1, 20)

# Phase 1 - First card
print("Your first card is: ", plyCard1)
print("Would you like to draw another card?")
plyResponse = str(input("y/n: "))

# Phase 2 - Second Card
if plyResponse == "y" or plyResponse == "Y":
    print("Your second card is is:", plyCard2)
    print("You have:", plyCard1 + plyCard2)
    print("CPU has:", cpuCard)

    # Phase 3 - Who won?
    if (plyCard1 + plyCard2) > cpuCard and plyCard1 + plyCard2 <= 21:
        print("**You win**")
    else:
        print("**CPU Wins**")
else:
    print("You have:", plyCard1)
    print("CPU has:", cpuCard)
    if plyCard1 > cpuCard:
        print("**You win**")
    else:
        print("**CPU Wins**")

###########################################################################

# A program to calculate tax based on a single input of hours worked.

# Store Constants
RATE_OF_PAY = float(35.00)
OVERTIME_PAY = float(50.00)
MAX_HOURS = int(39)
TAX_RATE_ONE = float(0.21)
TAX_BAND_ONE = int(18000/52)
TAX_RATE_TWO = float(0.42)
TAX_BAND_TWO = int(49000/52)

# Hours worked
hours = float(input("Input hours worked this week: "))
standardPay = float(hours * RATE_OF_PAY)
overtimePay = float((hours - MAX_HOURS) * OVERTIME_PAY)

# Check if we need overtime pay
if hours >= MAX_HOURS:
    income = standardPay + overtimePay
else:
    income = standardPay

# Not enough pay for tax
if income < TAX_BAND_ONE:
    netPay = income
    tax = 0

# Enough pay for tax bracket one
elif income < TAX_BAND_TWO:
    tax = (TAX_RATE_ONE * (income - TAX_BAND_ONE))
    netPay = income - tax

# Enough pay for tax bracket two
elif income >= TAX_BAND_TWO:
    tax = (TAX_RATE_ONE * TAX_BAND_ONE) + (TAX_RATE_TWO * (income - TAX_BAND_ONE))
    netPay = income - tax

else:
    pass

# Print data
print(hours, "Hours Worked")
print(round(standardPay, 2), "Standard Pay")

if hours >= MAX_HOURS:
    print(round(overtimePay, 2), "Overtime Pay")
    print(round(overtimePay, 2) + round(standardPay, 2), "Gross Pay")
else:
    print(round(standardPay, 2), "Gross pay")

print("-----------------")
print(round(tax, 2), "Total Tax")
print("-----------------")
print(round(netPay, 2), "Net Pay")


