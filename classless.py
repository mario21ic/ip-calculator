#!/usr/bin/env python
# Usage:   ./ipcalc.py ip prefix ips_amount
# Example: ./ipcalc.py 192.168.10.15 20 100

import sys

from lib.clase import get_clase
from lib.rango import get_rango, get_direccion_red, get_direccion_broadcast, get_primera_direccion, get_ultima_direccion, classless_porcion_host, classless_porcion_red, classless_wildcard
from lib.net_host import get_net_host
from lib.mask import get_mask


my_ip = sys.argv[1]
my_prefix = int(sys.argv[2])
my_qty = int(sys.argv[3])

n = classless_porcion_host(my_qty)
porcion_red = classless_porcion_red(n)
print("Porcion de Host:", n)
print("Porcion de Red: 32 - %s = %s" % (n, porcion_red))
print("Prefix: /%s" % porcion_red)
print("IPs:", my_qty)

print("="*6)

my_mask = get_mask(porcion_red)
print("Mask:", my_mask)
print("Wildcard:", classless_wildcard(my_mask))

print("="*6)

direccion_red = get_direccion_red(my_ip, n)
print("direccion de red:", direccion_red)
direccion_broadcast = get_direccion_broadcast(my_ip, n)
print("direccion de broadcast:", direccion_broadcast)

print("="*6)

print("primera direccion disponible:", get_primera_direccion(direccion_red))
print("ultima direccion disponible:", get_ultima_direccion(direccion_broadcast))

"""
Notes:
Inspirado en: http://labvirtual.webs.upv.es/ipcalc.html

TODO:
- Direccion de subred
- Direccion ip, mask y subred en binario
"""
