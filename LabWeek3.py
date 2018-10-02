# Sean Brooks
# X00152000

######################################################################################

# A function to convert a given time into seconds.

# Gather Data
timeHMS = input("Input time in format: HHMMSS ")
timeHours = int(timeHMS[:2])
timeMins = int(timeHMS[2:4])
timeSecs = int(timeHMS[4:])

# Display gathered data
print(timeHours, "Hours", timeMins, "minutes, and", timeSecs, "seconds", end=" ")

# Convert and display converted data in a print function
print("is", (timeHours*3600)+(timeMins*60)+timeSecs, " seconds.")

# Alternately, store converted data as a variable and display variables
timeHoursConverted = timeHours*3600
timeMinsConverted = timeMins*60
print("is", timeHoursConverted + timeMinsConverted + timeSecs, " seconds.")


######################################################################################

# A function to convert seconds into readable Hours, Minutes and Seconds.

# Gather Data
totalSeconds = int(input("Input the time in seconds: "))

# Flat divide hours then subtract from total seconds, repeat for minutes.
getHours = (totalSeconds//3600)
totalSeconds -= (getHours*3600)
getMinutes = (totalSeconds//60)
totalSeconds -= (getMinutes*60)

# Print the results in HHMMSS format.
print("End Result:", getHours, "Hours,", getMinutes, "minutes and", totalSeconds, "seconds")

######################################################################################

# A function to calculate Al's profits after VAT on a
# given number of fish and chips sales.

# Variables and Data
fishCost = float(4.50)
chipCost = float(2.80)
fishAmount = int(input("Input the number of Fish sold: "))
chipAmount = int(input("Input the number of Chips sold: "))

# Store each total as a variable.
alFishTotal = float(fishCost*fishAmount)
alChipTotal = float(chipCost*chipAmount)

# Calculate and show Al's total income
alMoneyTotal = round((alChipTotal + alFishTotal), 2)
print("Al's total income is", alMoneyTotal)

# Calculate 9% of Al's total and subtract it from his profits.
alVAT = round((alMoneyTotal/100)*9, 2)
print("Al's VAT is", alVAT)
print("Al's income after VAT is", round((alMoneyTotal - alVAT), 2))

# Save Al's profits and display them
alProfit = round((alMoneyTotal - alVAT)/2, 2)
print("Al's profits after expenses come to", alProfit)

######################################################################################

# A function to encrypt a five-letter word with a Caesar Cipher

# Gather Data
preCipher = input("Input a five letter word, in lowercase: ")
keyCipher = int(input("Input the encryption key: "))

# Fetch string index, convert to ASCII decimals and apply cipher
key01 = chr(ord(preCipher[0])+keyCipher)
key02 = chr(ord(preCipher[1])+keyCipher)
key03 = chr(ord(preCipher[2])+keyCipher)
key04 = chr(ord(preCipher[3])+keyCipher)
key05 = chr(ord(preCipher[4])+keyCipher)

# Print converted results
print("Your ciphered word is:", key01+key02+key03+key04+key05)
