def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
    'switchport mode trunk',
    'switchport trunk native vlan 999',
    'switchport trunk allowed vlan']

    result = []
    for interface, vlan in trunk.items():
        result.append(f"interface {interface}")
        for command in trunk_template:
            if 'allowed vlan' in command:
                result.append(f"{command} {','.join(map(str, vlan))}")
            else:
                result.append(command)
    return result

trunk_dict = { 'FastEthernet0/1':[10,20,30],
'FastEthernet0/2':[11,30],
'FastEthernet0/4':[17] }

print(generate_trunk_config(trunk_dict))
