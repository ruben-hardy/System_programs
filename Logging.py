import paramiko
import logging
def logie():
    logger = logging.getLogger("main")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("system.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("This is info")
    logger.info("This is debug")
    print(sub(568154,68655))
    logger.error("This is error")
def sub(a,b):
    llogger = logging.getLogger("main.secondary")
    llogger.info("This bullshit is unbelievable")
    c = a+b
    llogger.info("This %s plus this %s is %s" % (a,b,c))
    llogger.info("This is crap")
    print(a+b)
if __name__ == "__main__":
    logie()
