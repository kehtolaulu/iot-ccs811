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
                data = {
                    'eco2': self.ccs811.eco2,
                    'temperature': self.ccs811.temperature,
                    'temp_offset': self.ccs811.temp_offset,
                    'tvoc': self.ccs811.tvoc
                }
            except:
                pass
            else:
                self.observable.next(data)
            finally:
                time.sleep(self.interval)


    def subscribe(self, subscriber):
        self.observable.subscribe(subscriber)
