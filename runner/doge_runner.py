from trader import doge_trader
from trader import account_trader

import runner
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

        self.__account = account_trader.AccountTrader()

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

    def __is_time_to_buy(self, now):
        return self.__start_time <= now <= self.__sell_time

    def __is_time_to_sell(self, now):
        return self.__sell_time <= now <= self.__end_time

    def __has_to_buy(self, current_price, target_price_to_buy):
        return current_price >= target_price_to_buy

    def __has_to_sell(self, current_price, target_price_to_sell):
        return current_price >= target_price_to_sell

    def __can_buy(self, price):
        return price >= self.__doge.get_min_price_to_buy()

    def __can_sell(self):
        pass

    def run(self):
        while self.__run:
            now = datetime.datetime.now()

            current_krw_balance = self.__account.get_current_balance()
            current_coin_price = self.__doge.get_current_price()
            current_coin_balance = self.__doge.get_current_balance()

            if self.__is_time_to_buy(now):
                if self.__has_to_buy(current_coin_price, self.__target_buy_price) and self.__can_buy(current_krw_balance):
                    self.__doge.buy(current_krw_balance)
            elif self.__is_time_to_sell(now):
                if self.__has_to_sell(current_coin_price, self.__target_sell_price):
                    self.__doge.sell(current_coin_balance)
            else:
                # Time to init
                self.__init_time()
                self.__doge.__init__()
                time.sleep(10)
            time.sleep(10)

    def stop(self, signum, frame):
        self.__run = False


if __name__ == '__main__':
    runner = DogeRunner()
    runner.run()
