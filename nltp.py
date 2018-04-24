import nltk
import gensim
from gensim import corpora
from gensim.models import word2vec

paper_ids = open("papers.txt","r").read().split()
documents = {}
stop_words = set("for a of the and to in".split())
for paper in paper_ids:
    id_ = str(paper)
    documents[id_] = [word for word in open("document/"+str(paper),"r").read().lower().split() if word not in stop_words]
print(documents)
