from time import time

class Throttler(object):
    def __init__(self, rate=1.0, perSeconds=15.0):
        self.rate = rate
        self.perSeconds = perSeconds;
        self.allowance = rate;
        self.lastCheck = int(time());

    def check(self):
        current = int(time());
        timePassed = current - self.lastCheck;
        self.lastCheck = current;
        self.allowance += timePassed * (self.rate / self.perSeconds);

        if (self.allowance > self.rate):
            self.allowance = self.rate;

        if (self.allowance < 1.0):
            return False
        else:
            self.allowance -= 1.0;
            return True