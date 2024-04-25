import getpass
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
nr = InitNornir(config_file="config.yaml")

user = input("Please enter your username: ")
password = getpass.getpass()
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password

def pull_interface_info(task):
    interface_result = task.run(task=napalm_get, getters=["get_facts"])
    task.host["facts"] = interface_result.result
    
results = nr.run(task=pull_interface_info)
#print_result(results)
import ipdb
ipdb.set_trace()