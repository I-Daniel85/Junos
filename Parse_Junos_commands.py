from netmiko import ConnectHandler
import json

username = 'root'
password = 'toor123'
host = '192.168.188.128'

junos_device = {'device_type': 'juniper_junos', 'host': host, 'username': username, 'password': password}
dev = ConnectHandler(**junos_device)

command = "show chassis hardware"

command_output = dev.send_command(command + "| display json")

# type (command_output)
# command_output is a string

data_json = json.loads(command_output)
# type (data_json)
# data_json is a dictionnary

device_SN = data_json["chassis-inventory"][0]["chassis"][0]["serial-number"][0]['data']
print ("the SN of device " + host + " is: " + device_SN)