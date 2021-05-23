from config import config
from trader import trader
from lib import upbit
from lib import key_reader
from pandas import DataFrame


class DogeTrader(trader.Trader):

    def __init__(self) -> None:
        super().__init__()

        self.__upbit = upbit.UpBit()
        self.__key_reader = key_reader.KeyReader()

        self.__upbit.set_access_key(self.__key_reader.get_access_key())
        self.__upbit.set_secret_key(self.__key_reader.get_secret_key())

        self.__market_code = config.doge['market_code']
        self.__currency = config.doge['currency']
        self.__noise_ratio = config.doge['noise_ratio']
        self.__target_buy_price = config.default['buy_price']
        self.__target_sell_price = config.default['sell_price']

        self.set_target_buy_price()
        self.set_target_sell_price()

    def buy(self, price=0):
        return self.__upbit.order(self.__market_code, 'bid', volume=None, price=price, order_type='price').json()

    def sell(self, volume=0):
        return self.__upbit.order(self.__market_code, 'ask', volume=volume, price=None, order_type='market').json()

    def get_order_info(self):
        return self.__upbit.order_chance(self.__market_code).json()

    def get_current_price(self):
        return self.__upbit.ticker(self.__market_code).json()[0]['trade_price']

    def get_current_balance(self):
        balances = self.__upbit.accounts().json()
        current_balance = None

        for balance in balances:
            if balance['currency'] == self.__currency:
                current_balance = balance

        return current_balance['balance']

    def get_target_buy_price(self):
        return self.__target_buy_price

    def get_target_sell_price(self):
        return self.__target_sell_price

    def set_target_buy_price(self, count=2):
        day_candles = DataFrame.from_dict(self.__day_candle(count))

        today = day_candles.iloc[0]
        yesterday = day_candles.iloc[1]
        yesterday_volatility_range = yesterday['high_price'] - yesterday['low_price']

        self.__target_buy_price = today['opening_price'] + (yesterday_volatility_range * self.__noise_ratio)

    def set_target_sell_price(self):
        self.__target_sell_price = self.__target_buy_price

    def __day_candle(self, count=1):
        return self.__upbit.day_candle(market_code=self.__market_code, count=count).json()
