# Daniel Mc Callion
# A program that asks a user to enter a positive integer and then
# outputs the succesive values of the following calculation.
# If the number is even divide it by two, if it is odd multiply it by
# three and add one. Repeats until the current number is one.

numbers = []

current_number = int(input("Please enter a positive integer: "))

numbers.append(current_number)

while current_number != 1:

    if current_number % 2 == 0:
        current_number /= 2
    else:
        current_number = (current_number * 3) + 1

    numbers.append(current_number)

print(numbers)
