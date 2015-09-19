#!/usr/bin/env python3
__author__ = 'shiroyp'
from urllib.request import urlopen
from argparse import ArgumentParser
import csv
import io

parser = ArgumentParser(description='Converts the currency as per current exchange rate')
parser.add_argument('-f', '--from', default='EUR')
parser.add_argument('-t', '--to', default='INR')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = (vars(parser.parse_args()))
from_currency = args['from']
to_currency = args['to']

URL = 'http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=' + from_currency + to_currency +'=X'
webpage = urlopen(URL)
datareader = csv.reader(io.TextIOWrapper(webpage))
# readdata = webpage.read()
# csvdata = csv.reader(readdata.decode())
for row in datareader:
    print ('1 %s = %s %s' % (from_currency, row[1], to_currency))
