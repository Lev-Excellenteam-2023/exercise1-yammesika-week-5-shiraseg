from datetime import datetime
import random


def user_input(num):
    """ in this function we get the user input in a specific format"""
    while True:
        try:
            date = input(f"Please enter {num} date. PLease enter in this format: YYYY-MM-DD\n")
            date = datetime.strptime(date, '%Y-%m-%d').date()
            return date
        except ValueError:
            print("wrong format")


date1 = user_input("a")
date2 = user_input("another")
# creates a new 
if date1 > date2:
    rand_date = date1 + (date2 - date1) * random.random()
else:
    rand_date = date2 + (date1 - date2) * random.random()

# for checking if the random date is in monday or not we used the weekday() method
# weekday start with monday (=0) and end with sunday(=6)
if rand_date.weekday() == 0:
    print("I don't have vinaigrette!\nThe random date is:")
else:
    print("I don't have vinaigrette!\nThe random date is:")
print(rand_date)
