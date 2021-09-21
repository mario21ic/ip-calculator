#!/usr/bin/env python
# Usage:   ./subnets.py ip prefix
# Example: ./subnets.py 192.168.10.15 20

import sys

from lib.clase import get_clase
from lib.rango import get_rango, get_direccion_red, get_direccion_broadcast, get_primera_direccion, get_ultima_direccion, classless_porcion_host, classless_porcion_red, classless_wildcard
from lib.net_host import get_net_host, get_ip_qty
from lib.mask import get_mask


my_ip = sys.argv[1]
my_prefix = int(sys.argv[2])

porcion_red = my_prefix
porcion_host = 32 - porcion_red # TODO
ip_qty = get_ip_qty(porcion_host)

print("Porcion de Red: %s" % porcion_red)
print("Porcion de Host: 32 - %s = %s" % (porcion_red, porcion_host))
print("Prefix: /%s" % porcion_red)
print("IPs:", ip_qty)

print("="*6)

my_mask = get_mask(porcion_red)
print("Mask:", my_mask)
print("Wildcard:", classless_wildcard(my_mask))

print("="*6)

direccion_red = get_direccion_red(my_ip, porcion_host)
print("direccion de red:", direccion_red)
direccion_broadcast = get_direccion_broadcast(my_ip, porcion_host)
print("direccion de broadcast:", direccion_broadcast)

print("="*6)

print("primera direccion disponible:", get_primera_direccion(direccion_red))
print("ultima direccion disponible:", get_ultima_direccion(direccion_broadcast))

"""
Notes:
Inspirado en https://mxtoolbox.com/subnetcalculator.aspx

TODO:
- Refactor and unit tests
- Direccion de subred
- Direccion ip, mask y subred en binario
"""
