#!/usr/bin/env python
__author__ = 'shiroyp'
from urllib import urlopen
from argparse import ArgumentParser
import csv
from json import load

#Parsing the arguments passed to the script
parser = ArgumentParser(description='Converts the currency as per current exchange rate')
parser.add_argument('-f', '--from', default='EUR')
parser.add_argument('-t', '--to', default='INR')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = (vars(parser.parse_args()))
from_currency = args['from']
to_currency = args['to']

#From Yahoo Finance
URL = 'http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=' + from_currency + to_currency +'=X'
data = urlopen(URL)
csvdata = csv.reader(data)
for row in csvdata:
    print ('1 %s = %s %s' % (from_currency, row[1], to_currency))

"""From Heroku Rate Exchange App.
This is sometimes not working, seems like there is a limit on the no: of requests that you can make to this endpoint in a time period
Comment the below code block if you are getting errors for fetching exchange rates from heroku"""
def exchange_rate(from_currency,to_currency):
    URL = 'http://rate-exchange.herokuapp.com/fetchRate?from=' + from_currency + '&to=' + to_currency
    data = urlopen(URL)
    json_data = load(data)
    return (json_data['Rate'])
print ('Exchange rate from %s to %s is %s' % (from_currency, to_currency, exchange_rate(from_currency,to_currency)))
