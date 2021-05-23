from runner import runner
from trader import doge_trader

import time
import datetime
import signal


class DogeRunner(runner.Runner):

    def __init__(self) -> None:
        super().__init__()

        self.__run = True
        self.__start_time = None
        self.__sell_time = None
        self.__end_time = None

        self.__doge = doge_trader.DogeTrader()
        self.__target_buy_price = self.__doge.get_target_buy_price()
        self.__target_sell_price = self.__doge.get_target_sell_price()

        self.__init_time()

        signal.signal(signal.SIGINT, self.stop)

    def __init_time(self):
        now = datetime.datetime.now()
        self.__start_time = datetime.datetime(now.year, now.month, now.day)
        self.__end_time = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
        self.__sell_time = self.__end_time - datetime.timedelta(minutes=10)

    def run(self):
        while self.__run:
            now = datetime.datetime.now()

            current_price = self.__doge.get_current_price()
            current_balance = self.__doge.get_current_balance()

            if self.__start_time <= now <= self.__sell_time:
                # Time to buy
                if current_price > self.__target_buy_price:
                    # self.__doge.buy()
                    pass
            elif self.__sell_time <= now <= self.__end_time:
                # Time to sell
                if current_price > self.__target_sell_price:
                    # self.__doge.sell()
                    pass
            else:
                # Time to init
                self.__init_time()
                self.__doge.set_target_buy_price()
                self.__doge.set_target_sell_price()
                time.sleep(10)
            time.sleep(10)

    def stop(self, signum, frame):
        self.__run = False

