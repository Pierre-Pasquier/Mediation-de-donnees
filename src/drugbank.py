import os.path
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, KEYWORD, STORED
import xml.etree.ElementTree as ET
from whoosh.query import *
import whoosh.index as index
from whoosh.qparser import QueryParser



def CreateIndex():
    #Creating schema
    schema = Schema(Indication=TEXT(stored=True),Name=TEXT(stored=True), DrugInteraction=TEXT, Toxicity=TEXT(stored=True))

    #Creating a directory for the index
    if not os.path.exists("DrugBankIndex"):
        os.mkdir("DrugBankIndex")

    #Creating the index
    ix = create_in("DrugBankIndex", schema)

    #Creating a writer to add documents to the index
    writer = ix.writer()

    mytree = ET.parse('../Data/DRUGBANK/drugbank.xml')
    myroot = mytree.getroot()

    for x in myroot.findall('{http://www.drugbank.ca}drug'):
        name = ""
        name = x.find('{http://www.drugbank.ca}name').text
        indication = ""
        indication = x.find('{http://www.drugbank.ca}indication').text
        toxicity = ""
        toxicity = x.find('{http://www.drugbank.ca}toxicity').text
        DrugInteraction = ""
        DrugInteraction = x.find('{http://www.drugbank.ca}drug-interactions').text
        writer.add_document(Indication=indication, Name=name, DrugInteraction=DrugInteraction, Toxicity=toxicity)
    writer.commit()




def SearchIndication(name):
    ix = index.open_dir("DrugBankIndex")
    searcher = ix.searcher()

    parser = QueryParser("Name", ix.schema)
    query = parser.parse(name)

    results = searcher.search(query, limit=None)
    print(results[0])

def NomMedicamentToSE(liste_name):
    res = []

    # Ouvrir l'index et créer le searcher et le parser en dehors de la boucle for
    ix = index.open_dir("DrugBankIndex")
    searcher = ix.searcher()
    parser = QueryParser("Name", ix.schema)

    for name in liste_name:
        query = parser.parse(name)
        results = searcher.search(query, limit=None)

        for k in range(len(results)):
            try:
                res.append(results[k]['Toxicity'])
            except:
                pass

    return res


def ToxicitytoNomMedicament(liste_toxicity):
    ix = index.open_dir("DrugBankIndex")
    searcher = ix.searcher()
    parser = QueryParser("Toxicity", ix.schema)

    res = []
    for toxicity in liste_toxicity:
        toxicity = f"*{toxicity}*"
        query = parser.parse(toxicity)
        results = searcher.search(query, limit=None)
        res.extend([(result['Name'], 'drugbank') for result in results if 'Name' in result])

    # nous enlevons les doublons
    res = list(set(res))
    return res

#CreateIndex()
#print(NomMedicamentToSE(["Lepirudin"]))