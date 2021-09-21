from libs import key_reader
from libs import upbit

import json

access_key = key_reader.get_access_key()
secret_key = key_reader.get_secret_key()

upbit = upbit.UpBit()
upbit.set_access_key(access_key)
upbit.set_secret_key(secret_key)

"""마켓 코드 조회"""
# res = upbit.market_codes()
# print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

"""계정 정보 조회"""
res = upbit.accounts()
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

"""ORDER CHANGE 조회"""
res = upbit.order_chance(market_code='KRW-OMG')
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

"""Ticker 조회"""
res = upbit.ticker(market_code='KRW-OMG')
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

"""분 candle 조회"""
res = upbit.minute_candle(market_code='KRW-DOGE', count=2, unit=10)
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

"""일 candle 조회"""
res = upbit.day_candle(market_code='KRW-DOGE', count=2)
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

"""주 candle 조회"""
res = upbit.week_candle(market_code='KRW-DOGE', count=2)
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

"""월 candle 조회"""
res = upbit.month_candle(market_code='KRW-DOGE', count=2)
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

# order
res = upbit.order('1', '1', '1', '1', '1')
print(res.json())

# order_info
res = upbit.order_info('123')
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))

# order_cancel
res = upbit.order_cancel('123')
print(json.dumps(res.json(), indent=4, sort_keys=True, ensure_ascii=False))
