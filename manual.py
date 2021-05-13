from lib import key_reader
from lib import upbit

import json

key_reader = key_reader.KeyReader()
access_key = key_reader.get_access_key()
secret_key = key_reader.get_secret_key()

upbit = upbit.UpBit()
upbit.set_access_key(access_key)
upbit.set_secret_key(secret_key)

# accounts
res = upbit.accounts()
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

# market_codes
res = upbit.market_codes()
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

# ticker
res = upbit.ticker(market_code='KRW-DOGE')
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

# minute_candle
res = upbit.minute_candle(market_code='KRW-DOGE', count=2, unit=10)
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

# day_candle
res = upbit.day_candle(market_code='KRW-DOGE', count=2)
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

# week_candle
res = upbit.week_candle(market_code='KRW-DOGE', count=2)
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

# month_candle
res = upbit.month_candle(market_code='KRW-DOGE', count=2)
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))
