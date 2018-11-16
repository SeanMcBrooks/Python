# Sean Brooks
# x00152000

# A Program to calculate a fibonacci sequence.


# Inputs and Variables
userInput = int(input("Enter a number, 3 or above: "))

numOne = 1
numTwo = 1

# Checks and Equations
if userInput >= 2:
    print("1, 1", end="")
    for number in range(3, userInput+1, 1):
        fibonacci = (numOne + numTwo)
        print(",", fibonacci, end="")
        numOne = numTwo
        numTwo = fibonacci
elif userInput > 1:
    print("1, 1")
elif userInput > 0:
    print("1")
else:
    print("Invalid Input, must be an integer of 3 or above.")

######################################################################

# Sean Brooks
# x00152000

# A Program to replace blankspaces with %20

# Input
inputText = str(input("Input a sentence: "))

# For loop
for character in inputText:
    if character == " ":
        print("%20", end="")
    else:
        print(character, end="")

######################################################################

# Sean Brooks
# x00152000

# A Program to count a character in a given text.

# Inputs and Variables
inputText = str(input("Input a sentence: ")).lower()
inputChar = str("Force our way into the loop")
charCount = int(0)

# Check that the input is a single letter
while len(inputChar) != 1:
    inputChar = str(input("Input a single character: ")).lower()

# For loop and counter
else:
    for character in inputText:
        if character == inputChar:
            charCount += 1

    print(inputChar, "appears", charCount, "times.")
