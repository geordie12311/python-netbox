import time
from napalm import get_network_driver
from tabulate import tabulate
from rich import print as rprint
 
def main():
 
    devices = [
        {
            "host": "lab-sw1",
            "user": "cisco",
            "pass": "cisco123",
            "driver": "ios",
        },
        {
            "host": "lab-sw2",
            "user": "cisco",
            "pass": "cisco123",
            "driver": "ios",
        },
        {
            "host": "lab-sw3",
            "user": "cisco",
            "pass": "cisco123",
            "driver": "ios",
        },
    ]
    
    devices_table = [["Hostname", "Vendor", "Model", "Uptime", "Serial Number"]]
    devices_table_int = [["Hostname","Interface","is_up", "is_enabled", "Description", "Speed", "MTU", "Mac Address"]]

    rprint("\nCollecting the device facts & interface information from hosts.")           
    for dev in devices:
        driver = get_network_driver(dev["driver"]) #creating an object called driver and linking to the get_network_driver from napalm library 
        with driver(username=dev["user"], password=dev["pass"], hostname=dev["host"]) as device: #pulling the host details and using them with driver
          
            device_facts = device.get_facts()
            for facts in device_facts:                   
                devices_table.append([device_facts["hostname"],
                                    device_facts["vendor"],
                                    device_facts["model"],
                                    device_facts["uptime"],
                                    device_facts["serial_number"]
                                    ])
            
            device_interfaces = device.get_interfaces()
            for interface in device_interfaces:
                devices_table_int.append([device_facts["hostname"],
                                          interface,
                                          device_interfaces[interface]['is_up'],
                                          device_interfaces[interface]['is_enabled'],
                                          device_interfaces[interface]['description'],
                                          device_interfaces[interface]['speed'],
                                          device_interfaces[interface]['mtu'],
                                          device_interfaces[interface]['mac_address']
                                          ])
                
    rprint("\nCompleted collecting the data from the hosts.\n\n")
    time.sleep(1)
    rprint(tabulate(devices_table, headers="firstrow"))
    print("\n")
    rprint(tabulate(devices_table_int, headers="firstrow"))

 
if __name__ == '__main__':
    main()