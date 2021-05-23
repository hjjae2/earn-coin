from runner import runner
from trader import doge_trader

import signal


class DogeRunner(runner.Runner):

    def __init__(self) -> None:
        super().__init__()

        self.__run = True
        self.__doge = doge_trader.DogeTrader()

        signal.signal(signal.SIGINT, self.stop)

    def run(self):
        while self.__run:
            pass

    def stop(self, signum, frame):
        self.__run = False
