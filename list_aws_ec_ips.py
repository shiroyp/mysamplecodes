#!/usr/bin/env python

from urllib import urlopen
from json import load
regions = ['eu-west-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'ap-northeast-1', 'us-east-1', 'sa-east-1', 'us-west-1', 'us-west-2']

file = urlopen("https://ip-ranges.amazonaws.com/ip-ranges.json")
values = load(file)
for i in range(len(regions)):
    print regions[i]
    for each in values['prefixes']:
        if each['region'] == regions[i] and each['service'] == 'EC2':
            print each['ip_prefix']
    print " "
file.close()
