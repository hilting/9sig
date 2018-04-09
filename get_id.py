# coding: utf-8
import urllib.request
from xml.etree.ElementTree import *

keyword = "cancer"
baseURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=20&term="

def get_id(url):#論文IDを取得する
    result = urllib.request.urlopen(url)
    return result

def main():
    url = baseURL + keyword
    result = get_id(url)
    element = fromstring(result.read())
    filename = "idlist_"+keyword+".txt"
    f = open(filename, "w")
    for e in element.findall(".//Id"):
        f.write(e.text)
        f.write("\n")
    f.close()

if __name__ == "__main__":
    main()
