import sys

file = open(sys.argv[1], 'r')

for line in file:
    if not line.startswith('!'):
        print(line.rstrip())

file.close()