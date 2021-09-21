from config import config
from libs import upbit
from libs import key_reader
from libs import logger
from pandas import DataFrame


class Trader:
    def __init__(self) -> None:
        super().__init__()

        self.__upbit = upbit.UpBit()
        self.__upbit.set_access_key(key_reader.get_access_key())
        self.__upbit.set_secret_key(key_reader.get_secret_key())

        self.__currency = None
        self.__market_code = None

        self.__bid_fee = config.default['bid_fee']
        self.__ask_fee = config.default['ask_fee']
        self.__noise_ratio = config.default['noise_ratio']
        self.__min_price_to_buy = config.default['min_price_to_buy']
        self.__min_price_to_sell = config.default['min_price_to_sell']
        self.__target_buy_price = config.default['buy_price']
        self.__target_sell_price = config.default['sell_price']

        self.init_target_buy_price()
        self.init_target_sell_price()
        self.init_min_price_to_buy()
        self.init_min_price_to_sell()

    def buy(self, price=0):
        price = price * (1 - self.__bid_fee)
        result = self.__upbit.order(self.__market_code, 'bid', volume=None, price=price, order_type='price').json()
        if result is not False:
            logger.info("주문(매수) 시도 --> 결과 : {} 금액 : {}".format("성공", price))
        else:
            logger.info("주문(매수) 시도 --> 결과 : {} 금액 : {}".format("실패", price))
        return result

    def sell(self, volume=0):
        result = self.__upbit.order(self.__market_code, 'ask', volume=volume, price=None, order_type='market').json()
        if result is not False:
            logger.info("주문(매도) 시도 --> 결과 : {}".format("성공"))
        else:
            logger.info("주문(매도) 시도 --> 결과 : {}".format("실패"))
        return result

    def get_order_info(self):
        return self.__upbit.order_chance(self.__market_code).json()

    def get_current_price(self):
        return self.__upbit.ticker(self.__market_code).json()[0]['trade_price']

    def get_min_price_to_buy(self):
        return self.__min_price_to_buy

    def get_min_price_to_sell(self):
        return self.__min_price_to_sell

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

    def set_currency(self, currency):
        self.__currency = currency

    def set_market_code(self, market_code):
        self.__market_code = market_code

    def set_bid_fee(self, bid_fee):
        self.__bid_fee = bid_fee

    def set_ask_fee(self, ask_fee):
        self.__ask_fee = ask_fee

    def set_noise_ratio(self, noise_ratio):
        self.__noise_ratio = noise_ratio

    def set_min_price_to_buy(self, min_price_to_buy):
        self.__min_price_to_buy = min_price_to_buy

    def set_min_price_to_sell(self, min_price_to_sell):
        self.__min_price_to_sell = min_price_to_sell

    def set_target_buy_price(self, target_buy_price):
        self.__target_buy_price = target_buy_price

    def set_target_sell_price(self, target_sell_price):
        self.__target_sell_price = target_sell_price

    def init_target_buy_price(self, count=2):
        day_candles = DataFrame.from_dict(self.__day_candle(count))

        today = day_candles.iloc[0]
        yesterday = day_candles.iloc[1]
        yesterday_volatility_range = yesterday['high_price'] - yesterday['low_price']

        self.__target_buy_price = today['opening_price'] + (yesterday_volatility_range * self.__noise_ratio)

    def init_target_sell_price(self):
        self.__target_sell_price = self.__target_buy_price

    def init_min_price_to_buy(self):
        self.__min_price_to_buy = self.get_order_info()['market']['bid']['min_total']

    def init_min_price_to_sell(self):
        self.__min_price_to_sell = self.get_order_info()['market']['ask']['min_total']

    def __day_candle(self, count=1):
        return self.__upbit.day_candle(market_code=self.__market_code, count=count).json()
