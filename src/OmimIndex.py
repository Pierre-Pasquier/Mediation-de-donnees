import os.path
import time
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, KEYWORD, STORED
import xml.etree.ElementTree as ET
from whoosh.query import *
import whoosh.index as index
from whoosh.qparser import QueryParser
from whoosh.qparser import QueryParser
from whoosh import index


def CreateIndex():
    #Creating schema
    schema = Schema(CS=TEXT(stored=True),NO=TEXT(stored=True))

    #Creating a directory for the index
    if not os.path.exists("OMIMIndex"):
        os.mkdir("OMIMIndex")

    #Creating the index
    ix = create_in("OMIMIndex", schema)

    #Creating a writer to add documents to the index
    writer = ix.writer()


    f = open("../Data/OMIM/omim.txt", "r")
    lines = f.readlines()

    symptome = "Jaundice"

    cs = ""
    no = ""
    k = 0
    while k < len(lines):
        if lines[k][:10] == "*FIELD* NO":
            k += 1
            no = lines[k][:-1]
            while k < len(lines) and lines[k][:10] != "*FIELD* CS" and lines[k][:7] != "*RECORD*" :
                k+= 1
            k += 1
            while k < len(lines) and lines[k][0] != "*":
                if lines[k] != "\n":
                    if lines[k][-2:] == ":\n":
                        temp = lines[k][:-2]
                    else:
                        cs = lines[k] + '(' + temp + ')'
                        writer.add_document(CS=cs, NO=no)
                k += 1
        k += 1

    writer.commit()





def SearchNO(symptomes, searcher, parser):

    stopword = set(
        ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not",
         "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was",
         "will", "with", "from", "with", "which", "have", "has", "had", "can", "could", "may", "might", "must", "shall",
         "should", "will", "would", "do", "does", "did", "am", "is", "are", "was", "were", "be", "been", "being",
         "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or",
         "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
         "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
         "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
         "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",
         "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m",
         "o", "re", "ve", "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn", "haven", "isn", "ma", "mightn",
         "mustn", "needn", "shan", "shouldn", "wasn", "weren", "won", "wouldn"])

    res = []

    for symptome in symptomes:
        if symptome not in stopword:
            query = parser.parse(symptome)
            results = searcher.search(query, limit=None)

            for k in range(len(results)):
                res.append(results[k]['NO'])

    res = list(set(res))
    return res


def test():
    start_time = time.time()
    CreateIndex()
    print(len(SearchNO("Jaundice")))
    print("--- %s seconds ---" % (time.time() - start_time))

#CreateIndex()