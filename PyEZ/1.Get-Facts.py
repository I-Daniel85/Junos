from jnpr.junos import Device
from pprint import pprint

dev=Device(host='192.168.188.131', user='root', password='toor123')
dev.open()
pprint(dev.facts)
dev.close()