from config import config
from trader import trader
from lib import upbit
from lib import key_reader


class AccountTrader(trader.Trader):

    def __init__(self) -> None:
        super().__init__()

        self.__upbit = upbit.UpBit()
        self.__key_reader = key_reader.KeyReader()

        self.__upbit.set_access_key(self.__key_reader.get_access_key())
        self.__upbit.set_secret_key(self.__key_reader.get_secret_key())

        self.__market_code = config.krw['market_code']
        self.__currency = config.krw['currency']

    def buy(self):
        pass

    def sell(self):
        pass

    def get_current_price(self):
        pass

    def get_current_balance(self):
        balances = self.__upbit.accounts().json()
        current_balance = None

        for balance in balances:
            if balance['currency'] == self.__currency:
                current_balance = balance

        return current_balance['balance']

    def set_target_buy_price(self):
        pass

    def set_target_sell_price(self):
        pass
