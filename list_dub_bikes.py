#!/usr/bin/env python
__author__ = 'shiroyp'

from urllib import urlopen
from json import load

file = urlopen("http://api.citybik.es/dublinbikes.json")
values = load(file)

for each in values:
    if each['number'] ==87 or each['number'] ==19 or each['number'] ==39 or each['number'] ==5:
        # print each
        print "Station Name: " + each['name']
        print "Station Number: " + str(each['number'])
        print "Free Stands: " + str(each['free'])
        print "Available Bikes: " + str(each['bikes'])
        print
file.close()
