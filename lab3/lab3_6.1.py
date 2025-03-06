import sys

with open(sys.argv[1], 'r') as file:
    for line in file:
        parts = line.replace(',', '').split()
        print(f"Protocol: OSPF\n"
              f"Prefix: {parts[1]}\n"
              f"AD/Metric: {parts[2].strip('[]')}\n"
              f"Next-Hop: {parts[4]}\n"
              f"Last update: {parts[5]}\n"
              f"Outbound Interface: {parts[6]}\n")
