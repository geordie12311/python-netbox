import getpass
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure

nr = InitNornir(config_file="config.yaml")
user = input("Please enter your username: ")
password = getpass.getpass()
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password

def push_scp(task):
    task.run(task=napalm_configure, configuration="banner motd % THIS IS A TEST BANNER CREATED BY NAPALM FOR NETBOX DEVICES, UNAUTHORISED USERS WILL BE SHOT!!! %")

results = nr.run(task=push_scp)
print_result(results)