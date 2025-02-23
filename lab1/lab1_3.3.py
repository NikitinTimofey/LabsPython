CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
COMMANDS = CONFIG.split()
VLAN = COMMANDS[-1].split(',')
print(VLAN)