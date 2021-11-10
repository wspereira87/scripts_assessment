from netmiko import ConnectHandler

rtedspo0101 = {
    'device_type': 'juniper',
    'ip': '127.0.0.1',
    'port': '22224',
    'username': 't3533590',
    'password': '2c1p5Z7T@'
}

rtedspo0102 = {
    'device_type': 'juniper',
    'ip': '127.0.0.1',
    'port': '22225',
    'username': 't3533590',
    'password': '2c1p5Z7T@'
}

# Specify interface type like: "irb.", "ae11.", etc.
intf = "irb."

all_devices = [rtedspo0101, rtedspo0102]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print('Connecting to' + str(devices))
    f = open('vlans')
    for VLAN in f:
        VLAN = VLAN.strip()
        print("Analyzing VLAN " + str(VLAN))
        output = net_connect.send_command \
        ('show configuration interfaces {}'.format(intf) + str(VLAN) + '| display set')
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
