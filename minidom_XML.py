import xml.dom.minidom
class ReadXML():
    """""This is a class to read XML in human readable format"""
    def __init__(self, url):
        self.url = url
        xml = self.getXML(url)
        self.getTitles(xml)
    def getXML(self, url):
        f = url
        doc = xml.dom.minidom.parse(f)
        node = doc.documentElement
        books = doc.getElementsByTagName("Book")
        return books
    def getTitles(self, books):
        titles = []
        for book in books:
            titleObj = book.getElementsByTagName("title")[0]
            titles.append(titleObj)
            print("here")
        for title in titles:
            nodes = title.childNodes
            for node in nodes:
                if node.noteType == node.TEXT_NODE:
                    print(node.date)

if __name__ == "__main__":
    document = r"C:\Users\ruban.kumar\Desktop\sample.xml"
    ReadXML(document)