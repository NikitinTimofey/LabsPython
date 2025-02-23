command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

cmd_list1 = command1.split()
cmd_list2 = command2.split()
vlan1 = cmd_list1[-1].split(',')
vlan2 = cmd_list2[-1].split(',')

vlan_int1 = []
vlan_int2 = []

for i in vlan1:
    vlan_int1.append((int(i)))

for i in vlan2:
    vlan_int2.append((int(i)))

vlan_set1 = set(vlan_int1)
vlan_set2 = set(vlan_int2)

print(vlan_set1 & vlan_set2)
