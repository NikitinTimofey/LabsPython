def get_int_vlan_map(file):
    access_dict = {}
    trunk_dict = {}
    with open(file, 'r') as conf_file:
        intf = None
        for line in conf_file:
            if line.startswith('interface'):
                intf = line.split()[-1]
            elif 'switchport mode access' in line:
                access_dict[intf] = 1
            elif 'switchport access vlan' in line:
                access_dict[intf] = int(line.split()[-1])
            elif 'switchport trunk allowed vlan' in line:
                trunk_dict[intf] = list(map(int, line.split()[-1].split(',')))
    return access_dict, trunk_dict

print(get_int_vlan_map('config_sw2.txt'))