ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
route_part = ospf_route.replace(',', '').split()

ospf_dict = {
    'Protocol': 'OSPF',
    'Prefix': route_part[1],
    'AD/Metric': route_part[2].strip('[]'),
    'Next-Hop': route_part[4],
    'Last update': route_part[5],
    'Outbound Interface': route_part[6]
}

keys_list = list(ospf_dict.keys())
values_list = list(ospf_dict.values())

for i in range(len(ospf_dict)):
        print("{:25} {:15}".format(keys_list[i], values_list[i]))
