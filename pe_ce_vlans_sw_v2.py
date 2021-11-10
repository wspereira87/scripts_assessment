from netmiko import ConnectHandler

SWAVRJO0201 = {
    'device_type': 'cisco_ios',
    'ip': '127.0.0.1',
    'port': '22226',
    'username': 't3533590',
    'password': '5d3w8J1H#'
}
'''
rtedrjo0202 = {
    'device_type': 'juniper',
    'ip': '127.0.0.1',
    'port': '22226',
    'username': 't3533590',
    'password': '5d3w8J1H#'
}
'''
all_devices = [SWAVRJO0201]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print('Connecting to' + str(devices))
    f = open('vlans')
    for VLAN in f:
        VLAN=VLAN.strip()
        print("Analizing VLAN " + str(VLAN))
        output = net_connect.send_command('show spanning-tree vlan ' + str(VLAN) + '\n\n')
        output1 = net_connect.send_command('show interface status | include ' + '_' + str(VLAN) + '_'  + '\n\n')
        print(output)
        print(output1)