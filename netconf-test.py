import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
user = input("Enter your username: ")
password = getpass.getpass(prompt="Enter your password: ")
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password

def get_device_config(task):
    task.run(task=netconf_get_config, source="running")
    
results = nr.run(task=get_device_config)
print_result(results)