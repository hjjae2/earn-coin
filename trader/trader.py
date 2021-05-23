from abc import *


class Trader(metaclass=ABCMeta):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def sell(self):
        pass

    @abstractmethod
    def get_current_price(self):
        pass

    @abstractmethod
    def get_current_balance(self):
        pass

    @abstractmethod
    def set_target_buy_price(self):
        pass

    @abstractmethod
    def set_target_sell_price(self):
        pass
