#!/usr/bin/python

import sys

pathHitCount = 0
path_dic = {}

# Loop around the data
# parsing "GET /assets/css/the-associates.css HTTP/1.1" 
# max hit count in a file print that path

for line in sys.stdin:
    data = line.strip().split()
    
    if len(data) != 3:
        # Something has gone wrong. Skip this line.
        continue
    path = data[1]
     
    if not path in path_dic:
        path_dic[path] = 1
    else:
        path_dic[path] += 1
        

print len(path_dic)

