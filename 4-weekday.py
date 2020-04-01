# Daniel Mc Callion
# This program that outputs a message to state
# if today is weekday or not

# Import the datetime module from datetime to help get the current day
from datetime import datetime

# Tuple to store the days that are the weekend
weekend = ("Saturday", "Sunday")

# Use the datetime module to get the current day formatted as a string being the word for the day
current_day = datetime.today().strftime("%A")

# Check if the day returned for todays day is contained in the tuple containing the days that are the weekend
if current_day in weekend:
    # When it is the weekend, output a message to tell the user that its the weekend
    print("It is the weekend, yay!")
else:
    # When it is not the weekend, output a message to tell the user that its a weekday
    print("Yes, unfortunately today is a weekday.")
