import sys, json
from yahoo_finance import Share
from config import _symbols
from pprint import pprint

d = {}

for i in _symbols:
    symbol = Share(i)
    price = symbol.get_price()
    _jsonified = json.dumps(price)
    d[i] = _jsonified.replace('"','')

print(d)
