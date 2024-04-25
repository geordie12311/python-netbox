"""
Python script using Napalm getters to get facts.
Script using Netbox as Source of Truth
"""
#python script using nornir_napalm getters to get facts
#and check vendor and uptime of network devices 
import getpass
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")
#The above line is telling nornir where the config file is located
user = input("Enter your username: ")
password = getpass.getpass(prompt="Enter your password: ")
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password
#The above lines will prompt the user to enter their username and password and use that input to connect to the devices.

def get_facts(task):
    task.run(task=napalm_get, getters=["get_facts"])

results=nr.run(task=get_facts)
print_result(results)