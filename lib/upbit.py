import jwt
import uuid
import requests


class UpBit:
    __server_url = 'https://api.upbit.com'
    __access_key = None
    __secret_key = None

    def __init__(self) -> None:
        super().__init__()

    def __generate_headers(self):
        return {"Accept": "application/json"}

    def __generate_auth_headers(self):
        return {"Authorization": self.__generate_token()}

    def __generate_token(self):
        if self.__access_key is not None and self.__secret_key is not None:
            payload = {
                'access_key': self.__access_key,
                'nonce': str(uuid.uuid4()),
            }
            return 'Bearer {}'.format(jwt.encode(payload, self.__secret_key))
        return None

    def set_access_key(self, access_key=None):
        self.__access_key = access_key

    def set_secret_key(self, secret_key=None):
        self.__secret_key = secret_key

    def accounts(self):
        headers = self.__generate_auth_headers()
        return requests.get(self.__server_url + '/v1/accounts', headers=headers)

    def market_codes(self):
        headers = self.__generate_headers()
        return requests.get(self.__server_url + '/v1/market/all', headers=headers)

    def ticker(self, market_code=None):
        headers = self.__generate_headers()
        params = {'markets': market_code}
        return requests.get(self.__server_url + '/v1/ticker', headers=headers, params=params)

    def minute_candle(self, market_code=None, to=None, count=1, unit=1):
        if unit not in [1, 3, 5, 10, 15, 30, 60, 240]:
            return False

        headers = self.__generate_headers()
        params = {
            'market': market_code,
            'to': to,
            'count': count
        }
        return requests.get(self.__server_url + '/v1/candles/minutes/{}'.format(unit), headers=headers, params=params)

    def day_candle(self, market_code=None, to=None, count=1, converted_trade_price='KRW'):
        headers = self.__generate_headers()
        params = {
            'market': market_code,
            'to': to,
            'count': count,
            'convertingPriceUnit': converted_trade_price
        }
        return requests.get(self.__server_url + '/v1/candles/days', headers=headers, params=params)

    def week_candle(self, market_code=None, to=None, count=1):
        headers = self.__generate_headers()
        params = {
            'market': market_code,
            'to': to,
            'count': count
        }
        return requests.get(self.__server_url + '/v1/candles/weeks', headers=headers, params=params)

    def month_candle(self, market_code=None, to=None, count=1):
        headers = self.__generate_headers()
        params = {
            'market': market_code,
            'to': to,
            'count': count
        }
        return requests.get(self.__server_url + '/v1/candles/months', headers=headers, params=params)