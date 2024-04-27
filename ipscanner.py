"""
Python Script to scan a subnet and add active IP
addresses found to Netbox
"""
import networkscan
from netbox import NetBox
netbox = NetBox(host="192.168.1.20", port=80, use_ssl=False, auth_token="b26141e2f8e529817fa9644c4cf013ed56b02be7")

#Main fucntion
if __name__ == "__main__":
    
    #Define the network to scan
    my_network = "192.168.1.0/24"
    
    #create the object
    my_scan = networkscan.Networkscan(my_network)
    
    #Run the scan on the hosts using ping
    my_scan.run()
    
    #Display the ip addresses of all the hosts found by the scan
    for address in my_scan.list_of_hosts_found:
        print(address)
        #Add the active ip addresses found to Netbox
        netbox.ipam.create_ip_address(address)
