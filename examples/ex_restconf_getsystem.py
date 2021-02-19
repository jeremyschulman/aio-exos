from os import environ

from aioexos.restconf import Device

dev = Device(host=environ["NETWORK_DEVICE"],
             username=environ['NETWORK_USER'],
             password=environ['NETWORK_PASSWORD'])


# await dev.login()

url_system = '/rest/restconf/data/openconfig-system:system'
url_interfaces = '/rest/restconf/data/openconfig-interfaces:interface'
url_vlans = '/rest/restconf/data/openconfig-vlan:vlans'
