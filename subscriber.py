from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def on_next(self, message):
        pass
