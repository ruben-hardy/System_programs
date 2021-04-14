import urllib
import os
from threading import Thread
import sys

class Downloader(Thread):
    """Head Class"""
    def __init__(self, name, url):
        """Initialization"""
        Thread.__init__(self)
        self.name = name
        self.url = url
    def run(self):
        fpath = urllib.urlopen(self.url)
        fname = os.path.basename(self.url)
        path = r"C:\Users\ruban.kumar\Documents\Download" + fname
        with open(path, "wb") as fh:
            while True:
                chunk = fpath.read(1024)
                if not chunk:
                    break
                fh.write(chunk)
            print("%s downloaded file %s" % (self.name, fname))

def Tcreate(url):
    for num, url in enumerate(urls):
        num = "Thread %s" % num
        T = Downloader(num, url)
        T.start()
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf", "http://www.irs.gov/pub/irs-pdf/f1040a.pdf", "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf", "http://www.irs.gov/pub/irs-pdf/f1040es.pdf", "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    Tcreate(urls)