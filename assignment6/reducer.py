#!/usr/bin/python

import sys

pathHitCount = 0
req_dic = {}

# Loop around the data
# parsing "GET /assets/css/the-associates.css HTTP/1.1" 
# max hit count in a file print that path

for line in sys.stdin:
    data = line.strip()
    
    year = int(data)
    if not year in req_dic:
        req_dic[year] = 1
    else:
        req_dic[year] += 1
        

for k, v in req_dic.items():
    print("{0} {1}".format(k, v))

