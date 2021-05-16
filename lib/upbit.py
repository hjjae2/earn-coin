from urllib.parse import urlencode

import jwt
import uuid
import hashlib
import requests


class UpBit:
    __server_url = 'https://api.upbit.com'
    __access_key = None
    __secret_key = None

    def __init__(self) -> None:
        super().__init__()

    # Generate basic header
    def __generate_headers(self):
        return {"Accept": "application/json"}

    # Generate auth header
    def __generate_auth_headers(self, query=None):
        if query is not None:
            return {"Authorization": self.__generate_token(query)}
        return {"Authorization": self.__generate_token()}

    # Generate token
    def __generate_token(self, query=None):
        if self.__access_key is None or self.__secret_key is None:
            return None

        payload = {
            'access_key': self.__access_key,
            'nonce': str(uuid.uuid4()),
        }

        if query is not None:
            sha512 = hashlib.sha512()
            sha512.update(urlencode(query).encode())
            payload['query_hash'] = sha512.hexdigest()
            payload['query_hash_alg'] = 'SHA512'

        return 'Bearer {}'.format(jwt.encode(payload, self.__secret_key))

    # Set access key
    def set_access_key(self, access_key=None):
        self.__access_key = access_key

    # Set secret key
    def set_secret_key(self, secret_key=None):
        self.__secret_key = secret_key

    # 전체 계좌 조회
    def accounts(self):
        headers = self.__generate_auth_headers()
        return requests.get(self.__server_url + '/v1/accounts', headers=headers)

    # 주문
    def order(self):
        pass

    # 주문 취소
    def order_cancel(self):
        pass

    # 개별 주문 조회
    def order_info(self, uuid=None, identifier=None):
        if uuid is None and identifier is None:
            return False

        params = {}
        if uuid is not None:
            params['uuid'] = uuid
        elif identifier is not None:
            params['identifier'] = identifier

        headers = self.__generate_auth_headers(params)

        return requests.get(self.__server_url + '/v1/order', headers=headers, params=params)

    # 주문 리스트 조회
    def order_infos(self):
        pass

    # 주문 가능 정보
    def order_chance(self, market_code=None):
        params = {'market': market_code}
        headers = self.__generate_auth_headers(params)
        return requests.get(self.__server_url + '/v1/orders/chance', headers=headers, params=params)

    # 마켓 코드 조회
    def market_codes(self):
        headers = self.__generate_headers()
        return requests.get(self.__server_url + '/v1/market/all', headers=headers)

    # 시세 Ticker 조회
    def ticker(self, market_code=None):
        headers = self.__generate_headers()
        params = {'markets': market_code}
        return requests.get(self.__server_url + '/v1/ticker', headers=headers, params=params)

    # 시세 캔들 조회 (분)
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

    # 시세 캔들 조회 (일)
    def day_candle(self, market_code=None, to=None, count=1, converted_trade_price='KRW'):
        headers = self.__generate_headers()
        params = {
            'market': market_code,
            'to': to,
            'count': count,
            'convertingPriceUnit': converted_trade_price
        }
        return requests.get(self.__server_url + '/v1/candles/days', headers=headers, params=params)

    # 시세 캔들 조회 (주)
    def week_candle(self, market_code=None, to=None, count=1):
        headers = self.__generate_headers()
        params = {
            'market': market_code,
            'to': to,
            'count': count
        }
        return requests.get(self.__server_url + '/v1/candles/weeks', headers=headers, params=params)

    # 시세 캔들 조회 (월)
    def month_candle(self, market_code=None, to=None, count=1):
        headers = self.__generate_headers()
        params = {
            'market': market_code,
            'to': to,
            'count': count
        }
        return requests.get(self.__server_url + '/v1/candles/months', headers=headers, params=params)