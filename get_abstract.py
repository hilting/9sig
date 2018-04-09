# coding: utf-8
import urllib.request
from xml.etree.ElementTree import *

keyword = "cancer"
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
        url = baseURL + i + "&retmode=xml"
        result = get_xml(url)
        element = fromstring(result.read())
        for e in element.findall(".//AbstractText"):
            #print(e.text)#論文要旨を表示
            filename = "document" + i + "_" + keyword + ".txt"
            f2 = open(filename, "a") 
            f2.write(e.text)
            f2.write("\n")
            f2.close()

if __name__ == "__main__":
    main()
