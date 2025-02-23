IP = '192.168.3.1'

octet = list()

for i in IP.split('.'):
    octet.append(int(i))

print('{:<8} {:<8} {:<8} {:<8}'.format(
    octet[0], octet[1], octet[2], octet[3])
)

print('{:<08b} {:<08b} {:<08b} {:<08b}'.format(
    octet[0], octet[1], octet[2], octet[3])
)
