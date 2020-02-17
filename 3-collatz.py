# Daniel Mc Callion
# A program that asks a user to enter a positive integer and then
# outputs the succesive values of the following calculation.
# If the number is even divide it by two, if it is odd multiply it by
# three and add one. Repeats until the current number is one.

numbers = []

numbers.append(int(input("Please enter a positive integer: ")))

while numbers[-1] != 1:

    current_number = numbers[-1]

    if current_number % 2 == 0:
        current_number /= 2
    else:
        current_number = (current_number * 3) + 1

    numbers.append(current_number)

print(numbers)
