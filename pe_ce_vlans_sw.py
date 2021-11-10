import getpass
import telnetlib


# HOST = "netfindersbrasil1.ddns.net"
HOST = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass()
# password = "5d3w8J1H!"

'''
with SSHTunnelForwarder(
    ('186.228.3.251', 41001),
    ssh_username="italtel",
    ssh_password="supitaltel",
    # remote_bind_address=('192.168.253.205', 2323),
    local_bind_address=('0.0.0.0', 23333)

) as tunnel:
    tn = Telnet()
    tn.open('127.0.0.1', 23333)
    # telnet.close()
'''

tn = telnetlib.Telnet(HOST, port=23333)

# tn.write(b"t3533590\n")
# tn.read_until(b"Password: ")
# tn.write(b"5d3w8J1H!\n")
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    # tn.write(b"5d3w8J1H!\n")

# VLANS = open ('vlans')

tn.write(b"term length 0\n")
tn.write(b"show vlan br\n")
print(tn.read_all().decode('ascii'))
'''
for n in VLANS:
    n=n.strip()
    tn.write(b"show vlan br | i ^" + str(n).encode('ascii') + b"_" + b"\n")
    print(tn.read_all().decode('ascii'))
'''
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))
