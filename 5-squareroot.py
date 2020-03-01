# Daniel Mc Callion
# This program takes a positive floating point number
# and outputs an approximation of its square root

# Takes in a positive number, returns its square
def sqrt(positive_number):
    return positive_number ** 0.5

# Read in a number from the user
number_in = float(input("Please enter a positive number: "))

# Get the square root of the users number
square_out = sqrt(number_in)

# Print out the result
print(f"The square root of {number_in} is approx. {square_out:.1f}")
