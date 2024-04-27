from netbox import NetBox
import json
import requests
import ipcalc
import networkscan
API_TOKEN = "b26141e2f8e529817fa9644c4cf013ed56b02be7"
NB_URL = "http://192.168.1.20/"
HEADERS = {"Authorization": f"Token {API_TOKEN}", 
           "Content-Type": "application/json", 
           "Accept": "application/json"}
netbox = NetBox(host="192.168.1.20", port=80, 
                use_ssl=False, 
                auth_token="b26141e2f8e529817fa9644c4cf013ed56b02be7")

#Define the network to scan
my_network = "192.168.1.0/24"

#Get all ip addresses from the prefix
for ipaddress in ipcalc.Network(my_network):
    request_url = f"{NB_URL}/api/ipam/ip-addresses/?/q={ipaddress}/"
    ipaddress1 = requests.get(request_url, headers = HEADERS)
    netboxip = ipaddress1.json()
    print(netboxip)
    print(ipaddress)
    try:
        url = netboxip["results"][0]["url"]
        print(url)
    except:
        pass
    update = {
        "address": "{my_network}",
        "tags": {{"name":"labtag"}}
        }
    
    #If IP address is not already in netbox
    if netboxip["count"] == 0:
        pass
    else:
        change = requests.patch(url, headers = HEADERS, data=json.dumps(update))
        print(change)
        print(change.text)