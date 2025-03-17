ip = input("Введите IP-адрес: ")

octets = ip.split('.')
if len(octets) == 4 and all(o.isdigit() and 0 <= int(o) <= 255 for o in octets):
    first_octet = int(octets[0])
    if ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    elif 1 <= first_octet <= 127:
        print('unicast (class A)')
    elif 128 <= first_octet <= 191:
        print('unicast (class B)')
    elif 192 <= first_octet <= 223:
        print('unicast (class C)')
    elif 224 <= first_octet <= 239:
        print('multicast (class D)')
    else:
        print('unused')
else:
    print('Incorrect IPv4 address')