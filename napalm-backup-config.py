"""
Python script using Napalm ping to ping an address from all hosts
over the mgmt VRF. Script using Netbox as Source of Truth
"""
import getpass
from napalm import get_network_driver
from rich import print as rprint #importing print from rich and using it as rprintimport getpass
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_ping

nr = InitNornir(config_file="config.yaml")
user = input("Please enter your username: ")
password = getpass.getpass()
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password

def ping_test(task):
    task.run(task=napalm_ping, dest="192.168.1.10", vrf="MGMT")
#function is using the dest and optional vrf syntax to ping an address over
#the MGMT vrf from all hosts 

results = nr.run(task=ping_test)
print_result(results)