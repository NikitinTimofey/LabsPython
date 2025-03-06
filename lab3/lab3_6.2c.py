import sys

ignore = ['duplex', 'alias', 'Current configuration']

with open(sys.argv[1], 'r') as file, open(sys.argv[2], 'w') as file_cleared:
    for line in file:
        if not any(word in line for word in ignore):
            file_cleared.write(line)
