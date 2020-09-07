# Program: Ch 1 Ex 46
# Author:  Myron Moss
# Date: 08/07/2020
# Description: Calculates the time to run 5 miles, 10 miles, half marathon, and full marathon.

speed = int(input("Enter Running Speed(mph): "))
minutesPerMile = 60 // speed

print("It takes", minutesPerMile, "minutes to run a mile!")
print()
print("Calculation on Specific Distances")
print("=================================")

# TIME = (DISTANCE / SPEED) * 60

# Calculate for 5 Miles
time = (5 / speed) * 60  # Fill in the Formula to calculate TIME
hours = int(time / 60)  # Divide TIME BY 60 to get HOURS
minutes = int(time % 60)    # Remainder of Hours gives MINUTES
print("Five Miles:", hours, "hour(s),", minutes, "minutes")

# Calculate for 10 Miles
time = (10 / speed) * 60
hours = int(time / 60)
minutes = int(time % 60)
print("Ten Miles:", hours, "hour(s),", minutes, "minutes")

# Calculate for Half Marathon (13.1 Miles)
time = (13.1 / speed) * 60
hours = int(time / 60)
minutes = int(time % 60)
print("Half Marathon:", hours, "hour(s),", minutes, "minutes")

# Calculate for Full Marathon (26.2 Miles)
time = (26.2 / speed) * 60
hours = int(time / 60)
minutes = int(time % 60)
print("Full Marathon:", hours, "hour(s),", minutes, "minutes")