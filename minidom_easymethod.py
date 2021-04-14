import xml.dom.minidom
from xml.dom.minidom import Node

def ParseXML(file):
    doc = xml.dom.minidom.parse(file)
   # catalog = doc.documentElement
    cds = doc.getElementsByTagName('CD')
    n = 1
    #list = cds.getElement
    #print(list)
    for cd in cds:
        print("----------Compact Disk %s---------" % n)
        if cd.hasAttribute("id"):
            print(cd.getAttribute("id"))
        title = cd.getElementsByTagName('TITLE')[0]
        print("Title:\t\t %s" % title.childNodes[0].data)
        artist = cd.getElementsByTagName('ARTIST')[0]
        print("Artist:\t\t %s" % artist.childNodes[0].data)
        country = cd.getElementsByTagName('COUNTRY')[0]
        print("Country:\t\t %s" % country.childNodes[0].data)
        company = cd.getElementsByTagName('COMPANY')[0]
        print("Company :\t\t %s" % company.childNodes[0].data)
        year = cd.getElementsByTagName('YEAR')[0]
        print("Year:\t\t %s" % year.childNodes[0].data)
        price = cd.getElementsByTagName("PRICE")[0]
        print("Price:\t\t %s" % price.childNodes[0].data)
        n = n + 1
if __name__ =="__main__":
    file = r"C:\Users\ruban.kumar\Desktop\cd_catalog.xml"
    ParseXML(file)