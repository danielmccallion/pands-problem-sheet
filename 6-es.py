# Daniel Mc Callion
# This program takes an argument of a filename from the command line.
# It then reads that file and outputs the number of e's it contains.

import sys

e_count = 0


# Function to read a file and return the number of e's it contains
def read_number(file_to_read):
    with open(file_to_read) as f:
        count = int(f.read())
        return count


filename = str(sys.argv[1])
print(filename)
