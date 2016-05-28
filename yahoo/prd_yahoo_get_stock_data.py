# This script is ready to go.

import json, time, yahoo_finance, csv
ticker = "/opt/splunk/etc/apps/search/lookups/DEV_ALL_SP500_SYMBOLS.csv"
_file = open('/opt/splunk/etc/apps/search/bin/PRD_YAHOO_FIN_SHARES.OUTPUT', 'a')
while 1:
    time.sleep(300)
    try:
        with open(ticker, "r") as f:
            reader = csv.DictReader(f)
            l = []
            for i in reader:
                x = [i['Symbol']]
                for z in x: l.extend(x)
        for i in l:
            try:
                s = yahoo_finance.Share(i)
                s.refresh()
                d = {"symbol": None,"trade_datetime": s.get_trade_datetime(),"price": s.get_price(),"change": s.get_change(),"vol": s.get_volume(),
                     "prev_close": s.get_prev_close(),"open": s.get_open(),"avg_daily_vol": s.get_avg_daily_volume(),"stock_exchange": s.get_stock_exchange(),
                     "market_cap": s.get_market_cap(),"book_val": s.get_book_value(),"ebitda": s.get_ebitda(),"dividend_share": s.get_dividend_share(),
                     "dividend_yield": s.get_dividend_yield(),"earnings_share":s.get_earnings_share(),"days_high": s.get_days_high(),
                     "days_low": s.get_days_low(),"year_high": s.get_year_high(),"year_low": s.get_year_low(), "50day_moving_avg": s.get_50day_moving_avg(),
                     "200day_moving_avg": s.get_200day_moving_avg(),"price_earnings_ratio": s.get_price_earnings_ratio(),
                     "price_earnings_growth_ratio": s.get_price_earnings_growth_ratio(),"price_sales": s.get_price_sales(),
                     "price_book": s.get_price_book(),"short_ratio": s.get_short_ratio(),"info": s.get_info()}
                d['symbol'] = i
                d2 = (json.dumps(d))
                d3 = "BREAK"
                _file.write(d2)
                _file.write(d3)
            except Exception as e: print(e)
    except Exception as e: print(e)
_file.close()
