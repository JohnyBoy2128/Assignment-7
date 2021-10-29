#   Calendar program that allows the user to enter a day, month, and year, and give back info on the days in the month, and the days left in the year
#   John Paul Cannon
#   10 - 27 - 21

# function for whether year is a leap year
def leap_year(y):
	if (y % 4 == 0 and y % 100 != 0):   # checks if year is just divisible by 4 and not 100
		return 1
	elif (y % 400 == 0):   # adds years divisible by 400 to leap years
		return 1
	else:   # this is not a leap year
		return 0

# function to find the number of days in a month
def number_of_days(m, y):
	# array that holds the number of days in each month, adds 1 to Feb if a leap year
	daysInMonths = [31, 28 + leap_year(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return daysInMonths[m - 1]


# function to find the days left in the year
def days_left(d, m, y):
	



# inputs for day, month, year
print("Please enter a date")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

# input for whether to get days in month, or get days to end of the year
print("Menu:")
print("1) Calculate the number of days in the given month. ")
print("2) Calculate the number of days left in the given year.")
userChoice = input("")

# conditional for what to do depending on user input
if (userChoice == "1"):
	print(number_of_days(month, year))
