import os.path
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, KEYWORD, STORED
import xml.etree.ElementTree as ET
from whoosh.query import *
import whoosh.index as index
from whoosh.qparser import QueryParser

from keg import CreateIndex_keg, SearchIndication



def CreateIndex_chem():
    #Creating schema
    schema = Schema(StytchID=TEXT(stored=True),ATC=TEXT(stored=True))

    #Creating a directory for the index
    if not os.path.exists("../ChemIndex"):
        os.mkdir("../ChemIndex")

    #Creating the index
    ix = create_in("../ChemIndex", schema)

    #Creating a writer to add documents to the index
    writer = ix.writer()

    f = open("../Data/STITCH - ATC/chemical.sources.v5.0.tsv", "r")
    lines = f.readline()

    StytchId = ""
    ATC = ""
    k = 0
    working = False
    while lines:
        if k>=11:
            j=1
            while lines[j] != "\t":
                j+=1
            StytchId = lines[0:j]

            j+=1
            l = j
            while lines[l] != "\t":
                l+=1
            l += 1
            j = l
            while lines[l] != "\t":
                l+=1
            if lines[j:l] == "ATC":
                working = True
                l += 1
                ATC = lines[l:]

                StytchId = StytchId.replace("CIDm", "")
                writer.add_document(StytchID=StytchId, ATC=ATC)


            elif working:
                break


        k += 1
        lines = f.readline()

    writer.commit()




def SearchIndication_chem(StytchId):
    ix = index.open_dir("../ChemIndex")
    searcher = ix.searcher()
    res = []
    for elt in StytchId:
        parser = QueryParser("StytchID", ix.schema)
        elt = elt.replace("CID1", "")
        query = parser.parse(elt)
        results = searcher.search(query, limit=None)
        for k in range(len(results)):

            res.append(results[k]['ATC'])
    return res

#print("Result= " + str(SearchIndication_chem(["CID00002016"])))
def test():
    print("Lancement")
    #CreateIndex_chem()
    print("Index créé")
    #SearchIndication("CID00003269")
    print("Fin")


def Search_Name(StytchId):
    Atc = SearchIndication_chem(StytchId)
    return SearchIndication(Atc)


CreateIndex_chem()
#print(Search_Name("CID00003269"))

