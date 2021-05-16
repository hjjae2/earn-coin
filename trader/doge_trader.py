from config import config

from lib import upbit
from lib import key_reader

from trader import trader


class DogeTrader(trader.Trader):

    def __init__(self) -> None:
        super().__init__()

        self.__upbit = upbit.UpBit()
        self.__key_reader = key_reader.KeyReader()

        access_key = self.__key_reader.get_access_key()
        secret_key = self.__key_reader.get_secret_key()

        self.__upbit.set_access_key(access_key)
        self.__upbit.set_secret_key(secret_key)

        self.__ticker = None
        self.__day_candle = None
        self.__market_code = config.doge['market_code']

    def buy(self):
        # TODO
        pass

    def sell(self):
        # TODO
        pass

    def ticker(self):
        self.__ticker = self.__upbit.ticker(market_code=self.__market_code).json()

        return self.__ticker

    def day_candle(self):
        self.__day_candle = self.__upbit.day_candle(market_code=self.__market_code, count=1).json()

        return self.__day_candle
