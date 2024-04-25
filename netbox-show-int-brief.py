import os
import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

user = input("Enter your username: ")
password = getpass.getpass(prompt="Enter your password: ")
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password
#The above lines will prompt the user to enter their username and password and use that input to connect to the devices.

def use_netbox_as_nornir_inventory_source(task):
    task.run(task=send_command, command="show ip interface brief")

results = nr.run(task=use_netbox_as_nornir_inventory_source)
print_result(results)