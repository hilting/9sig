# coding: utf-8
import urllib.request
from xml.etree.ElementTree import *

def get_xml(url):#論文情報を取得する
    result = urllib.request.urlopen(url)
    return result

def ids_to_list(idfile):
    idlist = []
    f = open(idfile,"r")
    for i in f.readlines():
        idlist.append(i.strip())
    f.close()
    return idlist

def main():
    keyword = "all"
    idfile  = "nohup.out"
    baseURL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id="
    idlist = ids_to_list(idfile)
    for i in idlist:
        filename = "document" + i + "_" + keyword + ".txt"
        url = baseURL + i + "&rettype=abstract"  #"&retmode=xml"
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
