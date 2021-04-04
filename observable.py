from subscriber import Subscriber


class Observable:
    def __init__(self):
        self.subscribers = []


    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)


    def next(self, message):
        for subscriber in self.subscribers:
            subscriber.on_next(message)
