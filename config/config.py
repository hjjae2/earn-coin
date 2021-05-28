import os


default = {
    'buy_price': 99999999999,
    'sell_price': 99999999999,
    'access_key_path': os.path.dirname(os.path.abspath(__file__)) + '/access.key',
    'secret_key_path': os.path.dirname(os.path.abspath(__file__)) + '/secret.key',
}

krw = {
    'market_code': 'KRW',
    'currency': 'KRW',
}

doge = {
    'market_code': 'KRW-DOGE',
    'currency': 'DOGE',
    'noise_ratio': 0.5,
    'bid_fee': 0.0005,
    'ask_fee': 0.0005,
    'min_price_to_buy': 5000,
    'min_price_to_sell': 5000,
}

eos = {
    'market_code': 'KRW-EOS',
}

ripple = {
    'market_code': 'KRW-XRP',
}