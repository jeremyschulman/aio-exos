import asyncio
from os import environ

from aioexos.restconf import Device

dev = Device(
    host=environ["NETWORK_DEVICE"],
    username=environ["NETWORK_USER"],
    password=environ["NETWORK_PASSWORD"],
)


async def run():
    await dev.login()


url_system = "/openconfig-system:system"
url_interfaces = "/openconfig-interfaces:interface"
url_vlans = "/openconfig-vlan:vlans"


asyncio.run(run())
