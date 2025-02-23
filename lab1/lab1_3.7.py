MAC = 'AAAA:BBBB:CCCC'
octet = MAC.split(':')
mac_bin = []

for i in octet:
    mac_bin.append(bin(int(i, 16)))

print(mac_bin)
