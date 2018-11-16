# Sean Brooks
# x00152000

# Add the numbers between 1000 and 1500inl. with a while loop

# Start at 999 for inclusive 1000
counter = 999
totalCounter = 0

print("Count -> Total")

while counter < 1500:
    counter += 1
    totalCounter += counter
    print(counter, end=" -> ")
    print(totalCounter)

################################################################################

# Sean Brooks
# x00152000

# Input 2 numbers to a while loop, read and sum them in the loop

# Set variables to force into loop
input1 = 0
input2 = 0

# Set force to 0 and 0 because you couldn't add two 0's anyway
while input1 == 0 and input2 == 0:
    input1 = float(input("Input One: "))
    input2 = float(input("Input Two: "))
    sumResult = input1 + input2

# Calculate and print average outside the loop
averageResult = sumResult / 2
print("Average:", averageResult)


################################################################################

# Sean Brooks
# x00152000

limit = int(input("Enter Input: "))

# Three counters
counter = 0
evenCounter = 0
oddCounter = 0

# Increase counter to limit, add even and odd numbers to their respective counters.
while counter < limit:
    counter += 1
    if counter % 2 == 0:
        evenCounter += counter
    else:
        oddCounter += counter

# Display Results
print("Odd Sum:", oddCounter)
print("Even Sum:", evenCounter)

'''
Pen and paper check with input as 10:
1 + 3 + 5 + 7 + 9 = 25
0 + 2 + 4 + 6 + 8 + 10 = 30

Program result with input as 10:
25
30
'''

################################################################################

# Sean Brooks
# x00152000

# Set variable to force into loop
input1 = 1

# Counter
sumCounter = 0
averageCounter = 0

# While loop
while input1 >= 0:
    input1 = float(input("Input: "))
    if input1 >= 0:  # To prevent a negative number being added when leaving the loop
        sumCounter = sumCounter + input1
        averageCounter += 1
        print("Sum: ", sumCounter)

# Print results
print("Final Sum: ", sumCounter)
print("Average:,", sumCounter / averageCounter)

################################################################################

# Sean Brooks
# x00152000

# A program to check a string's word count using blankspaces.
wordInput = str(input("Feed me words: "))

# Start both counters at 0
spaceCount = 0
characterCounter = 0

# While loop counter with an if to compare against a blankspace.
while characterCounter < len(wordInput):
    if wordInput[characterCounter] == " ":
        spaceCount += 1
    characterCounter += 1

# One more word than space, assuming correct english format.
print("Space count:", spaceCount)
print("Word Count:", spaceCount + 1)

# Program gets really weird then there's numbers in the paragraph.
