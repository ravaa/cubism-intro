#!/usr/bin/python3

from urllib import request
import json
import sys

stocks_list = sys.argv[1:]
base_url = 'https://www.google.com/finance/getprices?q=%s&i=60&p=1d&f=d,c'

for stock in stocks_list:
	ts_data = []

	page       = request.urlopen(base_url % stock.upper()).read()
	price_data = page.decode().split('\n')[8:-1]
	
	for line in price_data:
		ts, price = line.split(',')
		ts_data.append([int(ts), float(price)])

	with open('data/%s.json' % stock.upper(), 'w') as f:
		json.dump(ts_data, f)

	print("Fetched data for %s" % stock.upper())