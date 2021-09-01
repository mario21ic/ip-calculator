#!/usr/bin/env python

def get_clase(my_ip):
    mydecimal = my_ip.split(".")
    first_byte = int(mydecimal[0])
    clase = ""
    if first_byte <= 127:
        clase = "A"
    elif first_byte >= 128 and first_byte <= 191:
        clase = "B"
    elif first_byte >= 192 and first_byte <= 223:
        clase = "C"
    elif first_byte >= 224 and first_byte <= 239:
        clase = "D"
    elif first_byte >= 240 and first_byte <= 255:
        clase = "E"

    return clase
