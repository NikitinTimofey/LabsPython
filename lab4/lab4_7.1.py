def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/12':10,
    'FastEthernet0/14':11,
    'FastEthernet0/16':17}
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
    'switchport access vlan',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable']

    result = []
    for interface, vlan in access.items():
        result.append(interface)
        for command in access_template:
            if 'vlan' in command:
                result.append(f"{command} {vlan}")
            else:
                result.append(command)
    return result

access_dict = { 'FastEthernet0/12':10,
'FastEthernet0/14':11,
'FastEthernet0/16':17,
'FastEthernet0/17':150 }

print(generate_access_config(access_dict))