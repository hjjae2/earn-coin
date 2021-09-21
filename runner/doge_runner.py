from trader import trader
from trader import account
from libs import logger
from runner import runner
from config import config

import time
import datetime
import signal


class DogeRunner(runner.Runner):
    def __init__(self) -> None:
        super().__init__()

        self.__account = account.AccountTrader()

        self.__trader = trader.Trader(config.doge)
        self.__target_buy_price = self.__trader.get_target_buy_price()
        self.__target_sell_price = self.__trader.get_target_sell_price()

        logger.log("TARGET BUY PRICE : {} | TARGET SELL PRICE : {}"
                   .format(self.__target_buy_price, self.__target_sell_price))

        signal.signal(signal.SIGINT, self.stop)

    def __can_buy(self, price):
        return price >= self.__trader.get_min_price_to_buy()

    def __can_sell(self):
        pass

    def run(self):
        while self._run:
            now = datetime.datetime.now()

            current_krw_balance = self.__account.get_current_balance()
            current_coin_price = self.__trader.get_current_price()
            current_coin_balance = self.__trader.get_current_balance()

            logger.log("CURRENT KRW : {} | CURRENT COIN PRICE : {} | CURRENT COIN BALANCE : {}"
                       .format(current_krw_balance, current_coin_price, current_coin_balance))

            if super().is_time_to_buy(now):
                if super().has_to_buy(current_coin_price, self.__target_buy_price) and self.__can_buy(current_krw_balance):
                    self.__trader.buy(current_krw_balance)
                    logger.info("[매수 완료] KRW : {}".format(current_krw_balance))
            elif super().is_time_to_sell(now):
                if super().has_to_sell(current_coin_price, self.__target_sell_price):
                    self.__trader.sell(current_coin_balance)
                    logger.info("[매도 완료] COIN BALANCE : {}".format(current_coin_balance))
            else:
                logger.log("INIT SETUP")
                super().init_time()
                self.__trader.__init__(config.doge)
                time.sleep(10)
            time.sleep(10)

    def stop(self, signum, frame):
        self._run = False


if __name__ == '__main__':
    runner = DogeRunner()
    runner.run()
