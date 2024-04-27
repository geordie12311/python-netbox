"""
Python Script using python-netbox
to pull back site details from Netbox
"""
from netbox import NetBox
netbox = NetBox(host="192.168.1.20", port=80, use_ssl=False, auth_token="b26141e2f8e529817fa9644c4cf013ed56b02be7")

nb_sites = netbox.dcim.get_sites()
print(nb_sites)