from abc import *


class Runner(metaclass=ABCMeta):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def run(self, *args):
        pass

    @abstractmethod
    def stop(self, *args):
        pass
