with open('CAM_table.txt', 'r') as file:
    for line in file:
        if any('.' in address for address in line):
            part = line.split()
            vlan = part[0]
            mac_address = part[1]
            ports = part[3]
            print(f"{vlan}   {mac_address}   {ports}")