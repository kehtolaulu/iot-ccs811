import time

from observable import Observable


class Css811Eco2(Observable):
    def __init__(self, ccs811, interval):
        self.ccs811 = ccs811
        self.interval = interval

        while not self.ccs811.data_ready:
            time.sleep(interval)


    def run(self):
        while True:
            try:
                eco2 = self.ccs811.eco2
            else:
                self.on_next({ 'eco2': eco2 })
            finally:
                time.sleep(interval)
