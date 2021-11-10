from netmiko import ConnectHandler

EDGE01 = {
    'device_type': 'juniper',
    'ip': '127.0.0.1',
    'port': '22224',
    'username': 't3533590',
    'password': '2c1p5Z7T@'
}

EDGE02 = {
    'device_type': 'juniper',
    'ip': '127.0.0.1',
    'port': '22225',
    'username': 't3533590',
    'password': '2c1p5Z7T@'
}

# Specify interface type like: "irb.", "ae11.", etc.
intf = 'irb.'

# Download network configuration.
all_devices = [EDGE01, EDGE02]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print('Connecting to device with port: ' + str(devices['port']))
    f = open('vlans')
    for VLAN in f:
        VLAN = VLAN.strip()
        print('Analyzing VLAN ' + str(VLAN))
        output = net_connect.send_command \
        ('show configuration interfaces {}'.format(intf) + str(VLAN) + '| display set')
        if output != '{master}':
            output1 = net_connect.send_command \
            ('show configuration | display set | match "{}'.format(intf) + str(VLAN) + '$"')
            output2 = net_connect.send_command \
            ('show configuration | display set | match {}'.format(intf) + str(VLAN) + '| match ospf')
            # output3 = net_connect.send_command \
            # ('show configuration | display set | match "vlan-id ' + str(VLAN) + '$"')
            # output4 = net_connect.send_command \
            # ('show configuration | display set | match "vlan-id-list ' + str(VLAN) + '$"')
            # output5 = net_connect.send_command \
            # ('show route table DCN.inet.0 protocol static output interface {}'.format(intf) + str(VLAN))
            # output5 = net_connect.send_command \
            # ('show route table inet.0 protocol static output interface {}'.format(intf) + str(VLAN))
            # output5 = net_connect.send_command \
            # ('show route table L3VPN_TIMGPRS.inet.0 protocol static output interface {}'.format(intf) + str(VLAN))
            # output5 = net_connect.send_command \
            # ('show route table TIMGPRS.inet.0 protocol static output interface {}'.format(intf) + str(VLAN))
            print(output)
            print(output1)
            print(output2)
            # print(output3)
            # print(output4)
            # print(output5)
        else:
            print('\n\n### VLAN NÃO EXISTENTE ###\n\n')
