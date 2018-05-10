# coding: utf-8
import urllib.request
from xml.etree.ElementTree import *

def get_id(url):#論文IDを取得する
    result = urllib.request.urlopen(url)
    return result

def main():
    keyword = "all[filter]"
    baseURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=28389011&term="
    url = baseURL + keyword
    result = get_id(url)
    element = fromstring(result.read())
    filename = "idlist_"+keyword+".txt"
    for e in element.findall(".//Id"):
        print (e.text)

if __name__ == "__main__":
    main()
