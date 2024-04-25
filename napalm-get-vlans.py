"""
Python script using Napalm getters to get the VLAN details
Script using Netbox as Source of Truth
"""
import getpass
from napalm import get_network_driver
from rich import print as rprint #importing print from rich and using it as rprintimport getpass
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="config.yaml")
user = input("Please enter your username: ")
password = getpass.getpass()
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password

def get_vlan(task):
    task.run(task=napalm_get, getters=["get_vlans"])

results=nr.run(task=get_vlan)
print_result(results)