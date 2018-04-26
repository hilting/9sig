import nltk
import gensim
from gensim import corpora
from gensim.models import word2vec
from collections import defaultdict

paper_ids = open("papers.txt","r").read().split()
corpus = {}
stop_words = set("for a of the and to in".split())
for paper in paper_ids:
    id_ = str(paper)
    words = open("document/"+str(paper),"r").read().lower().split()
    corpus[id_] = [word for word in words if word not in stop_words]

frequency = defaultdict(int)
for text in corpus.values():
    for token in text:
        frequency[token] += 1

processed_corpus = [[token for token in text if frequency[token] > 1] for text in corpus.values()]
print(processed_corpus)
dictionary = corpora.Dictionary(processed_corpus)
print (dictionary)

