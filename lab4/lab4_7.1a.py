def generate_access_config(access, psecurity = False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/12':10,
    'FastEthernet0/14':11,
    'FastEthernet0/16':17 }
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение F
    alse
    - если значение True, то настройка выполняется с добавлением шаблона port_secu
    rity
    - если значение False, то настройка не выполняется
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    access_template = ['switchport mode access',
    'switchport access vlan',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security']

    result = []
    for interface, vlan in access.items():
        result.append(interface)
        for command in access_template:
            if 'vlan' in command:
                result.append(f"{command} {vlan}")
            else:
                result.append(command)
        if psecurity:
            for command in port_security:
                result.append(command)
    return result

access_dict = { 'FastEthernet0/12':10,
'FastEthernet0/14':11,
'FastEthernet0/16':17,
'FastEthernet0/17':150 }

print(generate_access_config(access_dict))