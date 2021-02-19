from os import environ
from aioexos.jsonrpc import Device


dev = Device(host=environ["NETWORK_DEVICE"],
             username=environ['NETWORK_USER'],
             password=environ['NETWORK_PASSWORD'])

res = await dev.cli('show ports')


