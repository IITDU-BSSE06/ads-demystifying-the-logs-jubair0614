#!/usr/bin/python

import sys

pathHitCount = 0

# Loop around the data
# parsing "GET /assets/css/the-associates.css HTTP/1.1" 
# hit count in /assets/js/the-associates.js

for line in sys.stdin:
    data = line.strip().split()
    
    if len(data) != 3:
        # Something has gone wrong. Skip this line.
        continue
    path = data[1]    
    if path == "/assets/js/the-associates.js":
    	pathHitCount += 1
        

print pathHitCount


