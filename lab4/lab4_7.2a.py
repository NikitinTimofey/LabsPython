def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/1':[10,20],
    'FastEthernet0/2':[11,30],
    'FastEthernet0/4':[17] }
    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
    'switchport mode trunk',
    'switchport trunk native vlan 999',
    'switchport trunk allowed vlan']

    result = {}
    for interface, vlans in trunk.items():
        commands = []
        for command in trunk_template:
            if command == 'switchport trunk allowed vlan':
                commands.append(f"{command} {', '.join(map(str, vlans))}")
            else:
                commands.append(command)
        result[interface] = commands
    return result

trunk_dict = { 'FastEthernet0/1':[10,20,30],
'FastEthernet0/2':[11,30],
'FastEthernet0/4':[17] }

print(generate_trunk_config(trunk_dict))
