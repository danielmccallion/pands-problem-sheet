# Daniel Mc Callion
# A program that asks a user to enter a positive integer and then
# outputs the succesive values of the following calculation.
# If the number is even divide it by two, if it is odd multiply it by
# three and add one. Repeats until the current number is one.

# List to keep memory of all the values from the calculations
numbers = []

# Get from the user a positive number and cast the string to a value of type int
current_number = int(input("Please enter a positive integer: "))

# Add the number from the user as the first value in the list  
numbers.append(current_number)

# Check if the number is a 1, if not keep looping, if it is dont enter/leave the loop
while current_number != 1:

    # Check if the number is even, if it is divide it by 2
    if current_number % 2 == 0:
        current_number /= 2
    # If the number is odd, multiply it by 3 and then add 1
    else:
        current_number = (current_number * 3) + 1

    # Add the new number to the list of all calulations
    numbers.append(current_number)

# Print the list of all the succesive values from the users number until 1 was reached
print(numbers)
