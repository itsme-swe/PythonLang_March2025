from threading import *
from time import *


class Data:
    def __init__(self):
        self.data = 0
        self.flag = False
        self.lock = Lock()

    def put(self, d):
        while self.flag != False:
            pass
        self.lock.acquire()
        self.data = d
        self.flag = True
        self.lock.release()

    def get(self):
        while self.flag != True:
            pass
        self.lock.acquire()
        x = self.data
        self.flag = False
        self.lock.release()
        return x
