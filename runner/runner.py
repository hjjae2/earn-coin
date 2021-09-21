from abc import *

import datetime


class Runner(metaclass=ABCMeta):

    def __init__(self) -> None:
        super().__init__()

        self._run = True
        self._start_time = None
        self._end_time = None
        self._sell_time = None

        self.init_time()

    @abstractmethod
    def run(self, *args):
        pass

    @abstractmethod
    def stop(self, *args):
        pass

    def init_time(self):
        now = datetime.datetime.now()
        self._start_time = datetime.datetime(now.year, now.month, now.day)
        self._end_time = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
        self._sell_time = self._end_time - datetime.timedelta(minutes=10)

    def is_time_to_buy(self, now):
        return self._start_time <= now <= self._sell_time

    def is_time_to_sell(self, now):
        return self._sell_time <= now <= self._end_time

    def has_to_buy(self, current_price, target_price_to_buy):
        return current_price >= target_price_to_buy

    def has_to_sell(self, current_price, target_price_to_sell):
        return current_price >= target_price_to_sell
