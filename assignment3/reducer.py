#!/usr/bin/python

import sys
from urlparse import urlparse

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
    url = urlparse(path).path
     
    if not url in path_dic:
        path_dic[url] = 1
    else:
        path_dic[url] += 1
        

hit_count, full_path = max(zip(path_dic.values(), path_dic.keys()))
print full_path

#for k, v in path_dic.items():
#	     print("Code : {0}, Value : {1}".format(k, v))

