# import date from the datetime package

from datetime import date

# add a welcome message or title to make it more appealing to the user

print("Welcome to the Age Calculator!\n")

# make the function to calculate the age of the user

def calc_age(birthDate):
	today = date.today()
	age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
	return age 

# take the input from the user of the Date of birth details

yy = int(input("Please enter your year of birth: "))
mm = int(input("Please enter your month of birth: "))
dd = int(input("Please enter your day of birth: \n"))

# call the function to calculate the age

age = calc_age(date(yy, mm, dd))

# print the age

print(f"\nYour age is {age}.")

# Burger King is having an offer where kids under the age of 12 can eat for free! Let's see if you can too...

if age > 12:
	print("\nSorry! You can't eat at Burger King for free.")
else:
	print("Fantastic! Your meal at Burger King will be free.")

# remember to save the program with ctrl + s
# run it in the command prompt