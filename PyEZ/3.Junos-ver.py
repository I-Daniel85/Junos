from jnpr.junos import Device

with Device(host='192.168.188.131', user='root', password='toor123') as dev:
    print (dev.cli("show version", warning=False))