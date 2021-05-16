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
