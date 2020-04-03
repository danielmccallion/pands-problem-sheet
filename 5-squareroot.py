# Daniel Mc Callion
# This program takes a positive floating point number
# and outputs an approximation of its square root using Newtons method for square roots

# Takes in a positive number, returns its square using Newtons method
def sqrt(positive_number):

    # Set the first guess to be the number itself 
    approx_root = positive_number

    # The precision determines how close of an approximation to try get with Newtons method
    precision = 0.0000000001

    # Assign the difference a value higher than the precision before the while loop so it enters
    difference = 1

    # Loops until the approx_root is less than the value of the precision
    while difference > precision:

        # Newtons method for approximating the square root
        approx_root = (approx_root + positive_number/ approx_root) / 2

        # Get the positive value of the difference of the appoximate root
        difference = abs(positive_number - approx_root * approx_root)

    return approx_root


# Read in a number from the user
number_in = float(input("Please enter a positive number: "))

# Make sure the number entered is positive incase of a divide by zero error
number_in = abs(number_in)

# Get the square root of the users number
square_out = sqrt(number_in)

# Print out the result with the number of decimals to match the precision
print(f"The square root of {number_in} is approx. {square_out:.9f}")
