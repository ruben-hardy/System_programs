import random
import time
from threading import Thread
class Th(Thread):
    """Class creation"""
    def __init__(self, name):
        """Thread Initiation"""
        Thread.__init__(self)
        self.name = name
    def run(self):
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)
def head():
    for i in range(5):
        name = "Thread %s" % (i+1)
        mythread = Th(name)
        mythread.start()
if __name__ == "__main__":
    head()