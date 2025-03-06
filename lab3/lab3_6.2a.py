import  sys

file = open(sys.argv[1], 'r')
ignore = ['duplex', 'alias', 'Current configuration']

for line in file:
    if not line.startswith('!') and not any(word in line for word in ignore):
        print(line.rstrip())

file.close()
