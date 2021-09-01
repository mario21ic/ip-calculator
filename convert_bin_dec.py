#!/usr/bin/env python

import sys

from lib.convert import bin_dec


if len(sys.argv)==1:
    print("Usage:\n./convert_bin_dec.py 10000001 00001011 00001011 11101111")
else:
    for block in range(1, len(sys.argv)):
        print(bin_dec(sys.argv[block]), end=" ")

print("")
