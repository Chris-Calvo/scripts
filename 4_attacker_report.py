#!/usr/bin/python3
from geoip import geolite2
import os
import re
import time
import socket
import struct

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

def main():
    # Clears When Running
    os.system("clear")
    # Appends each failed attempt to dictionary
    counter("C:/Users/Chris/Downloads/syslog.log")
    # People make mistakes, clear out those who do not seem like a threat
    parse_dictionary(ipDict)
    # Sort dictionary based on number of attacks
    sortedVer = dict(sorted(ipDict.items(), key=lambda item: item[1]))

    # Print attack report header
    today = time.strftime("%m / %d / %Y")
    print("Attacker Report - ", today)
    print ("\n")
    print("COUNT            IP ADDRESS          COUNTRY")
    for item in sortedVer:
        count = sortedVer.get(item)
        #ip_as_bytes = bytes(map(int, item.split('.')))
        country = geolite2.lookup(item)
        print(count, "          ", item, "            ", country.country)

main()

    
