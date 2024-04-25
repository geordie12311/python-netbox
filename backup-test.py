"""
Python script to use Netbox as inventory and
backup running configuration from all the hosts
"""
import getpass
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file

BACKUP_PATH = "./configs"
#The above line is telling nornir where the backup directory is

nr = InitNornir(config_file="config.yaml")
#The above line is telling nornir where the config file is located
nr = nr.filter(platform="ios")
#The above line is filtering on specific platforms in this case ios

user = input("Enter your username: ")
password = getpass.getpass(prompt="Enter your password: ")
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password
#The above lines will prompt the user to enter their username and password and use that input to connect to the devices

def backup_config(task, path):
    device_config = task.run(
        task=napalm_get,
        getters=["config"]
    )

    task.run(
        task=write_file,
        content=device_config.result["config"]["running"],
        filename=f"{path}/{task.host}.txt",
    )
# The above function is using napalm getters to get running configs and save to file in the backups directory

result = nr.run(
    name="Backup Device Configuration", path=BACKUP_PATH, task=backup_config
)
#The above line is capturing the output and saving as a variable called "result"

print_result(result)
#The above line is printing the data catpured in "result" to the screen