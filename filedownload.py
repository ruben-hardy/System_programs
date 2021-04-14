from urllib import urlopen
from threading import Thread
import sys
import os

class Downloader(Thread):
    """Head Class"""
    def __init__(self, url, path):
        """Initialization"""
        Thread.__init__(self)
        self.url = url
        self.path = path

    def run(self):
        fpath = urlopen(self.url)
        fname = os.path.basename(self.url)
        path = "\\\\".join(self.path.split("\\")) + "\\" + fname
        with open(path, "wb") as fh:
            while True:
                chunk = fpath.read(1024)
                if not chunk:
                    break
                fh.write(chunk)
            #print("%s downloaded file %s" % (self.name, fname))
        return fname
def Tcreate(url, path=r"C:\Users\ruban.kumar\Documents\Download"):
    #for num, url in enumerate(urls):
        #num = "Thread %s" % num
        T = Downloader(url, path)
        T.start()
if __name__ == "__main__":
    url = raw_input("Enter the url to download file")
    Tcreate(url)