# Daniel Mc Callion
# This program  calculates somebody's Body Mass Index (BMI).
# The inputs are the person's height in centimetres and weight in kilograms.
# The output is their weight divided by their height in metres squared. 
# Expected outcome:
# Enter weight: 65
# Enter height: 180
# BMI is 20.06.

weight = int(input("Enter weight: "))
height = int(input("Enter height: "))

height_metres = height/100

height_squared = height_metres ** 2

bmi = weight / height_squared

print(f"BMI is {bmi:.2f}.")
