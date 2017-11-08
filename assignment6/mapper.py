#!/usr/bin/python

# Format of each line is:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/the-associates.css HTTP/1.1" 200 15779

import sys

for line in sys.stdin:
    data = line.strip().split('[')
    dateValue = data[1]
    onlyDate = dateValue.strip().split("/")
    onlyYear = onlyDate[2]
    hitDate = onlyYear.strip().split(":")
    year = hitDate[0]
    print year
