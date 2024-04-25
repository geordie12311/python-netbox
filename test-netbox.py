import getpass
from nornir import InitNornir
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

# it is not recommended to store username and password in automation script.
# in the next script we use environment variables to read the username and password.
user = input("Enter your username: ")
password = getpass.getpass(prompt="Enter your password: ")
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password
#The above lines will prompt the user to enter their username and password and use that input to connect to the devices.

def get_inventory_from_netbox(task):
    rprint(f"device name: {task.host}")
    rprint(f"device IP address: {task.host.hostname}")
    rprint(f"device platform: {task.host.platform}")
    rprint(f"device inventory data: {task.host.data}")

nr.run(task=get_inventory_from_netbox)