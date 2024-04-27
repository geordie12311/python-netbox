"""
Python Script using Python Netbox
to apull back device role information
from Netbox
"""
from netbox import NetBox
netbox = NetBox(host="192.168.1.20", port=80, use_ssl=False, auth_token="b26141e2f8e529817fa9644c4cf013ed56b02be7")

nb_device_role = netbox.dcim.get_device_roles()
print(nb_device_role)