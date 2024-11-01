import yaml


dlist = {'vSRX1':
             {'netmiko': {'device_type': 'juniper_junos', 'host': '', 'username': '', 'password': ''},
              'local_asn': '', 'neighbors': []},
        'vSRX2':
            {'netmiko': {'device_type': 'juniper_junos', 'host': '', 'username': '', 'password': ''},
             'local_asn': '', 'neighbors': []}}

""""Device 1"""
dlist['vSRX1']['netmiko']['host']=input("Please enter the IP address for first device: ")
dlist['vSRX1']['netmiko']['username']=input("Please enter username: ")
dlist['vSRX1']['netmiko']['password']=input("Please enter password for Device 1: ")
dlist['vSRX1']['local_asn']=input("Please enter local AS for Device 1: ")
device1 = {'interface': '', 'interface_description':'', 'asn':'', 'peer_ip': '', 'local_ip': ''}
device1['interface']=input('Please enter interface name for device 1: ')
device1['interface_description']=input('Please enter the description for the interface: ')
device1['asn']=input('Please enter the AS for device 1: ')
device1['peer_ip']=input('Please enter the peer IP for device 1: ')
device1['local_ip']=input('Please enter the local IP for device 1: ')
""""Device 2"""
dlist['vSRX2']['netmiko']['host']=input("Please enter the IP address for second device: ")
dlist['vSRX2']['netmiko']['username']=input("Please enter username: ")
dlist['vSRX2']['netmiko']['password']=input("Please enter password for Device 2: ")
dlist['vSRX2']['local_asn']=input("Please enter local AS for Device 2: ")
device2 = {'interface': '', 'interface_description':'', 'asn':'', 'peer_ip': '', 'local_ip': ''}
device2['interface']=input('Please enter interface name for device 2: ')
device2['interface_description']=input('Please enter the description for the interface: ')
device2['asn']=input('Please enter the AS for device 2: ')
device2['peer_ip']=input('Please enter the peer IP for device 2: ')
device2['local_ip']=input('Please enter the local IP for device 2: ')

dlist['vSRX1']['neighbors'].append(device1)
dlist['vSRX2']['neighbors'].append(device2)
with open('result1.yml', 'w') as yaml_file:
    yaml.dump(dlist, yaml_file, default_flow_style=False)


