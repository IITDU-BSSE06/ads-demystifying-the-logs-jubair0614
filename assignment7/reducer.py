#!/usr/bin/python

import sys
from urlparse import urlparse

pathHitCount = 0
req_dic = {}

# Loop around the data
# parsing "GET /assets/css/the-associates.css HTTP/1.1" 
# max hit count in a file print that path

for line in sys.stdin:
    data = line.strip().split()
    
    if len(data) != 3:
        # Something has gone wrong. Skip this line.
        continue
    request = data[0]
     
    if not request in req_dic:
        req_dic[request] = 1
    else:
        req_dic[request] += 1
        

for k, v in req_dic.items():
	print("{0} {1}".format(k, v))

