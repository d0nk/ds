import sys, json, time
from yahoo_finance import Share
from config import _symbols
from pprint import pprint

d = {}

while 1:
    time.sleep(300)
    for i in _symbols:
        symbol = Share(i)
        price = symbol.get_price()
        _jsonified = json.dumps(price)
        d[i] = _jsonified.replace('"','')

    data = str(d)
    try:
        with open ('/opt/splunk/bin/scripts/outputs/yahoo_get_shares_output.txt', 'a') as f:
            f.write(data)
    except Exception as e:
        print(e)
