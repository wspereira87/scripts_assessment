from netmiko import ConnectHandler

rtedrce0301 = {
    'device_type': 'juniper',
    'ip': '127.0.0.1',
    'port': '22224',
    'username': 't3533590',
    'password': '5d3w8J1H!'
}

rtedrce0302 = {
    'device_type': 'juniper',
    'ip': '127.0.0.1',
    'port': '22225',
    'username': 't3533590',
    'password': '5d3w8J1H!'
}

all_devices = [rtedrce0301, rtedrce0302]
#vlans = [100, 200, 201, 202, 508, 509, 516, 517, 518, 519, 900, 901, 1607, 1609, 1807, 1809]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print('Connecting to' + str(devices))
    f = open('vlans')
    for VLAN in f:
        VLAN=VLAN.strip()
        print("Analizing VLAN " + str(VLAN))
        output = net_connect.send_command('show configuration interfaces irb.' + str(VLAN) + '| display set')
        output1 = net_connect.send_command('show configuration | display set | match "irb.' + str(VLAN) + '$"')
        #output2 = net_connect.send_command('show configuration | display set | match "vlan-id ' + str(VLAN) + '$"')
        #output3 = net_connect.send_command('show configuration | display set | match "vlan-id-list ' + str(VLAN) + '$"')
        #output4 = net_connect.send_command('show route table DCN.inet.0 protocol static output interface irb.' + str(VLAN))
        #output4 = net_connect.send_command('show route table L3VPN_TIMGPRS.inet.0 protocol static output interface irb.' + str(VLAN))
        #output4 = net_connect.send_command('show route table VPNTI.inet.0 protocol static output interface irb.' + str(VLAN))
        #output4 = net_connect.send_command('show route table inet.0 protocol static output interface irb.' + str(VLAN))
        print(output)
        print(output1)
        #print(output2)
        #print(output3)
        #print(output4)
