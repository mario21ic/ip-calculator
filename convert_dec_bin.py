#!/usr/bin/env python
# Usage: ./convert_dec_bin.py 128.11.3.31

import sys

from lib.convert import dec_bin


mydecimal = sys.argv[1].split(".")
if len(mydecimal) == 4:
    for block in mydecimal:
        print(dec_bin(int(block)), end=" ")
else:
    print("Usage:\n ./convert_dec_bin.py 128.11.3.31")

print("")

