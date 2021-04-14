from queue import Queue
import os
from threading import Thread
import urllib.request
class Downloader(Thread):
    """Main class"""
    def __init__(self, queue, name):
        """Initializing Thread"""
        Thread.__init__(self)
        self.queue = queue
        self.name = name
    def run(self):
        #Getting url from queue
        url = self.queue.get()
        self.download_file(url)
        self.queue.task_done()
    def download_file(self, url):
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)
        path = r"C:\Users\ruban.kumar\Desktop\PDF_Download\\" + fname
        with open(path, "wb") as fh:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                fh.write(chunk)
            print("%s: File %s successfully downloaded " % (self.name, fname))
def head(urls):
    queue = Queue()
    for i in range(5):
        name = "Thread %s" % (i + 1)
        T = Downloader(queue, name)
        T.setDaemon(True)
        T.start()
    for url in urls:
        queue.put(url)
    queue.join()
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf", "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf", "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    head(urls)