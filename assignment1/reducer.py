#!/usr/bin/python

import sys

ipCount = 0

# Loop around the data
# get number of count in ip 10.99.99.186

for line in sys.stdin:
    data = line.strip()
    
    if data == "10.99.99.186":
    	ipCount += 1

print ipCount


