# Daniel Mc Callion
# This program  calculates somebody's Body Mass Index (BMI).
# The inputs are the person's height in centimetres and weight in kilograms.
# The output is their weight divided by their height in metres squared. 
# Expected outcome:
# Enter weight: 65
# Enter height: 180
# BMI is 20.06.

# Get weight and height as input from the user and cast as type int
weight = int(input("Enter weight: "))
height = int(input("Enter height: "))

# Change height in cm's to metres
height_metres = height/100

# Square the height value
height_squared = height_metres ** 2

# calculate bmi by dividing the weight value by the height squared
bmi = weight / height_squared

# Output the result formatted to two decimal points
print(f"BMI is {bmi:.2f}.")
