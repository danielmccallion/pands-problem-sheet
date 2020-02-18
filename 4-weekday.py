# Daniel Mc Callion
# This program that outputs a message to state
# if today is weekday or not

import datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

if datetime.datetime.today().strftime("%A") in weekend:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")