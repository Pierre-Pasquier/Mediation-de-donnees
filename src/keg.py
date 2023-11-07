import os.path
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, KEYWORD, STORED
import xml.etree.ElementTree as ET
from whoosh.query import *
import whoosh.index as index
from whoosh.qparser import QueryParser



def CreateIndex_keg():
    #Creating schema
    schema = Schema(ATC=TEXT(stored=True),Label=TEXT(stored=True))

    #Creating a directory for the index
    if not os.path.exists("KegIndex"):
        os.mkdir("KegIndex")

    #Creating the index
    ix = create_in("KegIndex", schema)

    #Creating a writer to add documents to the index
    writer = ix.writer()

    f = open("../Data/STITCH - ATC/br08303.keg", "r")
    lines = f.readlines()
    atc = ""
    Label = ""
    k = 9
    while k < len(lines):
        if lines[k][0] != "#" and lines[k][0] != "!":
            j=1
            while lines[k][j] == " ":
                j+=1
            l = j
            while lines[k][l] != " ":
                l+=1
            atc = lines[k][j:l]
            j = l
            while lines[k][j] == " ":
                j+=1
            Label = lines[k][j:-1]
            if "[" in Label:
                Label = Label[0:Label.find("[")]
            if "(" in Label:
                Label = Label[0:Label.find("(")]
            writer.add_document(ATC=atc, Label=Label)

        k += 1

    writer.commit()




def SearchIndication(atc):
    ix = index.open_dir("KegIndex")
    searcher = ix.searcher()

    parser = QueryParser("ATC", ix.schema)
    res = []
    for k in range(len(atc)):
        query = parser.parse(atc[k])
        results = searcher.search(query, limit=None)
        for r in results:
            res.append(r['Label'])
    return res

def test():
    print("Lancement")
    #CreateIndex_keg()
    print("Index créé")
    SearchIndication("D02721")
    print("Fin")

