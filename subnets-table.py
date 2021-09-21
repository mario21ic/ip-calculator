#!/usr/bin/env python
# Usage:   ./subnets-table.py ip prefix ips_requeridas
# Example: ./subnets-table.py 192.168.10.15 20 800

import sys

from lib.clase import get_clase
from lib.rango import get_rango, get_direccion_red, get_direccion_broadcast, get_primera_direccion, get_ultima_direccion, classless_porcion_host, classless_porcion_red, classless_wildcard, getN, get_subnet_direccion_red, get_subnet_direccion_broadcast
from lib.net_host import get_net_host, get_ip_qty
from lib.mask import get_mask


my_ip = sys.argv[1]
my_prefix = int(sys.argv[2])
ips_requeridas = int(sys.argv[3])

#porcion_host = 32 - porcion_red # TODO
porcion_host = getN(ips_requeridas)
porcion_red = 32 - porcion_host
ip_qty = get_ip_qty(porcion_host)

print("Porcion de Host: %s" % porcion_host)
print("Porcion de Red: 32 - %s = %s" % (porcion_host, porcion_red))
print("Prefix: /%s" % porcion_red)
print("IPs: 2^%s = %s" % (porcion_host, ip_qty))

print("="*6)

my_mask = get_mask(porcion_red)
print("Mask:", my_mask)
wildcard = classless_wildcard(my_mask)
print("Wildcard:", wildcard)

print("="*6)

direccion_red = get_subnet_direccion_red(my_ip, my_prefix)
print("direccion de red:", direccion_red)
direccion_broadcast = get_subnet_direccion_broadcast(direccion_red, wildcard)
print("direccion de broadcast:", direccion_broadcast)

print("="*6)

print("primera direccion disponible:", get_primera_direccion(direccion_red))
print("ultima direccion disponible:", get_ultima_direccion(direccion_broadcast))

"""
Notes:
Inspirado en https://mxtoolbox.com/subnetcalculator.aspx

TODO:
- Agregar tabla comenzando por el que requiere mas IPs (clase 7_1 1:02)
- Refactor and unit tests
- Direccion ip, mask y subred en binario
"""

