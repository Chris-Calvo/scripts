#!/usr/bin/python3
from geoip import geolite2
import os
import re

test = "Apr 15 00:00:04 spark sshd[7798]: Failed password for root from 218.25.208.92 port 20924 ssh2"
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
ipDict = {}

def counter(filename):
    try:
        with open(filename) as fhandle:
            for line in fhandle:
                if "Failed password for" in line:
                    tokens = line.split()
                    for token in tokens:
                        if re.search(regex, token):
                            if token not in ipDict:
                                ipDict[token] = 1
                            else:
                                ipDict[token] += 1
    except:
        return False

def parse_dictionary(dictionary):
    popList = []
    for ips in dictionary:
        if dictionary.get(ips) < 10:
            popList.append(ips)
    for item in popList:
        dictionary.pop(item)

counter("C:/Users/Chris/Downloads/syslog.log")
parse_dictionary(ipDict)
sorted = dict(sorted(ipDict.items(), key=lambda item: item[1]))
print(sorted)

    
