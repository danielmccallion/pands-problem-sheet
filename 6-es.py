# Daniel Mc Callion
# This program takes an argument of a filename from the command line.
# It then reads that file and outputs the number of e's it contains.

import sys


# Function to read a file and return the count of a letter it contains
def read_number(file_to_read, letter_to_search_for):
    with open(file_to_read) as f:
        # Count the occurences of the letter
        count = f.read().count(letter_to_search_for)
        return count


# Take the filename to read from the command line
filename = str(sys.argv[1])

# Read the file and return the number of e's
e_count = read_number(filename, "e")

# Print the resulting number of e's
print(e_count)
