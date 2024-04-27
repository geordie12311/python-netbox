import requests
import json

API_TOKEN = "{{ lookup('env', 'NETBOX_TOKEN') }}"
HEADERS = {'Authorization': f'Token {API_TOKEN}', 'Content-type': 'application/json','Accept': 'application/json'}
NB_URL = "{{ lookup('env', 'NETBOX_URL') }}"

device_name = "Test1"
name_of_interface = "Ethernet0/0"
description = "added by python"

#convert device_name to device_id
def request_devices(device_name):
    requests_url = f"{NB_URL}/api/dcim/devices/?q=(device_name)"
    devices = requests.get(requests_url, headers = HEADERS)
    result = devices.json()
    id = result["results"][0]["id"]
    return id
    print(result["results"][0]["id"])

#send POST request
def post_interfaces(device_name,name_of_interface):
    id = request_devices(device_name)
    request_url = f"{NB_URL}/api/dcim/devices/?q=(device_name)"
    interface_parameters = {
        "device": id,
        "name": name_of_interface,
        "description": description
        "type": "virtual",
        "enabled": True,
        "mode": "access"
        }
    
    new_device = requests.post(request_url, headers = HEADERS, json=interface_parameters)
    print(new_device.json())

post_interfaces(device_name,name_of_interface)

