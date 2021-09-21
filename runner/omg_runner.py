from trader import trader
from trader import account
from libs import logger
from runner import runner
from config import config

import time
import datetime
import signal


class OmgRunner(runner.Runner):
    def __init__(self) -> None:
        super().__init__()

        self.__run = True
        self.__start_time = None
        self.__end_time = None
        self.__sell_time = None
        self.__account = account.AccountTrader()

        self.__trader = trader.Trader(config.omg)
        self.__target_buy_price = self.__trader.get_target_buy_price()
        self.__target_sell_price = self.__trader.get_target_sell_price()

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
        return price >= self.__trader.get_min_price_to_buy()

    def __can_sell(self):
        pass

    def run(self):
        while self.__run:
            now = datetime.datetime.now()

            current_krw_balance = self.__account.get_current_balance()
            current_coin_price = self.__trader.get_current_price()
            current_coin_balance = self.__trader.get_current_balance()

            logger.log("TARGET BUY PRICE : {} | TARGET SELL PRICE : {}"
                       .format(self.__target_buy_price, self.__target_sell_price))
            logger.log("CURRENT KRW : {} | CURRENT COIN PRICE : {} | CURRENT COIN BALANCE : {}"
                       .format(current_krw_balance, current_coin_price, current_coin_balance))

            if self.__is_time_to_buy(now):
                if self.__has_to_buy(current_coin_price, self.__target_buy_price) and self.__can_buy(current_krw_balance):
                    self.__trader.buy(current_krw_balance)
                    logger.info("[매수 완료] KRW : {}".format(current_krw_balance))
            elif self.__is_time_to_sell(now):
                if self.__has_to_sell(current_coin_price, self.__target_sell_price):
                    self.__trader.sell(current_coin_balance)
                    logger.info("[매도 완료] COIN BALANCE : {}".format(current_coin_balance))
            else:
                logger.log("INIT SETUP")
                self.__init_time()
                self.__trader.__init__()
                time.sleep(10)
            time.sleep(10)

    def stop(self, signum, frame):
        self.__run = False


if __name__ == '__main__':
    runner = OmgRunner()
    runner.run()
