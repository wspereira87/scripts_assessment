from netmiko import ConnectHandler

### def declaration #########################################

def netmk_connection(port):
    return {
        'device_type': 'juniper',
        'ip': '127.0.0.1',
        'port': port,
        'username': 't3533590',
        'password': '2c1p5Z7T@'
    }


# Specify EDGE interface type like: "irb.", "ae11.", etc.
intf = 'irb.'


# Download network configuration.
device_ports = ['22224', '22225']

for port in device_ports:
    edge_device = netmk_connection(port)
    net_connect = ConnectHandler(**edge_device)
    print('Connecting to device with port: ' + port + "\n")
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
            print(output)
            print(output1)
            print(output2)
        else:
            print('\n\n### VLAN NÃO EXISTENTE ###\n\n')
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
        # print(output3)
        # print(output4)
        # print(output5)
