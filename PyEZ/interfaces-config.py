from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='192.168.188.131', user='root', password='toor123', gather_facts=False)
dev.open()

cu = Config(dev)
data = """interfaces { 
    ge-0/0/3 {
        description "MPLS interface";
        unit 0 {
            family mpls;
        }      
    } 
    ge-0/0/4 {
        description "MPLS interface";
        unit 0 {
            family mpls;
        }      
    }   
}
protocols {
    mpls { 
        interface ge-0/0/3; 
        interface ge-0/0/4;            
    }
}
"""
cu.load(data, format='text')
cu.pdiff()
if cu.commit_check():
   cu.commit()
else:
   cu.rollback()