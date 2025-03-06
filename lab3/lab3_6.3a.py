vlan = []
mac_address = []
ports = []

with open('CAM_table.txt', 'r') as file:
    for line in file:
        if any('.' in address for address in line):
            part = line.split()
            vlan.append(int(part[0]))
            mac_address.append(part[1])
            ports.append(part[3])

address = list(sorted(zip(vlan, mac_address, ports)))
print(f"{address}")