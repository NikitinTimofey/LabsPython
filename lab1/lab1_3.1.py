NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT2 = NAT.replace('Fast', 'Gigabyte')
print(NAT2)