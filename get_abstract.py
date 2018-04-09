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
    url = baseURL + idlist[0] + "&retmode=xml"
    result = get_xml(url)
    element = fromstring(result.read())
    for e in element.findall(".//AbstractText"):
        print(e.text)#論文要旨を表示

if __name__ == "__main__":
    main()
