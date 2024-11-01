from netmiko import ConnectHandler

print("Please enter IP address")
ip = input()
print("Please enter hostname")
hostname = input()
print("Please enter password!")
password = input()

virtual_srx = {
    'device_type': 'juniper',
    'host': ip,
    'username': hostname,
    'password': password,
    'port': 22,  #
}
net_connect = ConnectHandler(**virtual_srx)


def version():
    output = net_connect.send_command("show system information1")
    print(output)


def interfaces():
    output = net_connect.send_command("show interfaces terse")
    print(output)


def interface():
    print("Please enter interface name")
    interface = str(input())
    output = net_connect.send_command("show interfaces {} terse".format(interface))
    print(output)


while True:
    print("Welcome to Juniper UI")
    print("Please choose an option from the list")
    print("1. Display Juniper Version")
    print("2. Display all interfaces")
    print("3. Display a specific interface")
    choice = int(input())
    if choice == 1:
        version()
    elif choice == 2:
        interfaces()
    elif choice == 3:
        interface()
    else:
        break
