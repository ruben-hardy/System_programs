import time
from threading import Thread
class Vechicle(Thread):
    """
    Main class
    """
    def __init__(self, car, brand, cls, typ):
        """
        Initializing the thread
        :param car:
        :param brand:
        :param cls:
        :param typ:
        """
        Thread.__init__(self)
        self.car = car
        self.brand = brand
        self.cls = cls
        self.typ = typ
    def run(self):
        msg = "I have a %s %s %s %s car" % (self.car, self.brand, self.cls, self.typ)
        print(msg)
def mythread():
    lst = ["BMW", "AUDI", "LAMBORGHINI", "FERRARI"]
    car = ["M5", "R8", "Huracan", "LaFerrari"]
    cls = "sports"
    typ = ["sedan", " ", "super", "exotic"]
    brand = "bmw"
    for i in range(len(lst)):
        mythread = Vechicle(lst[i], car[i], cls, typ[i])
        mythread.start()
        time.sleep(10)

if __name__ == "__main__":
    mythread()