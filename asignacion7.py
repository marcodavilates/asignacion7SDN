import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
payload=response.json()

response = requests.get(
    'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/',
    headers={'X-Auth-Token':payload["Token"]})
payload=response.json()
devices = []
print("Family"+ "                                  ""Hostname"+ "                     "+"IP Address"+ "                     "+"Last Update"+ "                      "+"Status")
for device in payload["response"]:
    devices.append([device["family"], device["hostname"], device["managementIpAddress"], device["lastUpdated"], device["reachabilityStatus"]])

for device in devices:
    print(device[0] + "                     "+device[1] + "                     "+device[2] + "                     "+device[3] + "                      "+device[4] + "           ")

