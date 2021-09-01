#!/usr/bin/env python

def bin_dec(mybinario) -> int:
    """
    bits_value = []
    for x in range(8):
        bits_value.append(2**x)
    bits_value.reverse()
    """
    bits_value = [2**x for x in range(8)]
    bits_value.reverse()

    result = 0
    x = 0
    for b in mybinario:
        if b=="1":
            result += int(bits_value[x])
        x+=1
    return result

def dec_bin(mydecimal):
    bits_value = [2**x for x in range(8)]
    bits_value.reverse()

    result = ""
    suma = 0
    for d in bits_value:
        suma = suma + int(d)
        if suma <= mydecimal:
            result += "1"
        else:
            suma = suma - d
            result += "0"
    return result

def ip_bin(my_ip):
    octetos = my_ip.split(".")
    bits = ""
    for block in octetos:
        #print("block:", block)
        bits += str(dec_bin(int(block)))
    bits = list(bits)
    return bits

def fill_last_n(bits, n, replace_with):
    for x in range(n):
        index = len(bits)-(x+1)
        #print("index", index)
        bits[index] = replace_with
    return bits
