# Daniel Mc Callion
# This program that outputs a message to state
# if today is weekday or not

from datetime import datetime

weekend = ("Saturday", "Sunday")

current_day = datetime.today().strftime("%A")

if current_day in weekend:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")
