# coding: utf-8
import urllib.request
from xml.etree.ElementTree import *

keyword = "protein"
idfile = "idlist_"+keyword+".txt"
baseURL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id="

def get_xml(url):#論文情報を取得する
    result = urllib.request.urlopen(url)
    return result

def main():
    idlist = []
    f = open(idfile,"r")
    for i in f.readlines():
        idlist.append(i.strip())
    f.close()
    for i in idlist:
        print(i)
        f4 = open("ids", "a")
        f4.write(i + "\n")
        f4.close()
        filename = "document" + i + "_" + keyword + ".txt"
        url = baseURL + i + "&retmode=xml"
        result = get_xml(url)
        re_strip = result.read().decode().replace("<i>","").replace("</i>","").replace("<sup>","").replace("</sup>","").replace("<sub>","").replace("</sub>","").replace("<b>","").replace("</b>","")
        f3 = open("raw_"+filename, "a")
        f3.write(re_strip)
        f3.close()
        element = fromstring(re_strip)
        #print(result.read())
        for e in element.findall(".//AbstractText"):
            #print(e.text)#論文要旨を表示
            f2 = open(filename, "a") 
            f2.write(e.text)
            #f2.write("\n")
            f2.close()

if __name__ == "__main__":
    main()
