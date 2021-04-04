import time

from observable import Observable


class Ccs811Eco2:
    def __init__(self, ccs811, interval):
        self.observable = Observable()
        self.ccs811 = ccs811
        self.interval = interval

        while not self.ccs811.data_ready:
            time.sleep(interval)


    def run(self):
        while True:
            try:
                eco2 = self.ccs811.eco2
            except:
                pass
            else:
                self.observable.next({ 'eco2': eco2 })
            finally:
                time.sleep(self.interval)


    def subscribe(self, subscriber):
        self.observable.subscribe(subscriber)
