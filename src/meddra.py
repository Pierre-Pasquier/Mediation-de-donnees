import csv
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, KEYWORD, STORED
import xml.etree.ElementTree as ET
from whoosh.query import *
import whoosh.index as index
from whoosh.qparser import QueryParser
import os
def get_stitch_ID_by_CUI(liste_CUI):
    IDs = set()

    # Utiliser un ensemble pour la liste_CUI afin de vérifier rapidement si un CUI est présent
    liste_CUI_set = set(liste_CUI)

    with open('../Data/Medra/meddra_all_indications.tsv', 'r') as tsv_file:
        tsv_reader = csv.DictReader(tsv_file, delimiter='\t')
        for row in tsv_reader:
            if row["CUI"] in liste_CUI_set:
                IDs.add(row["StitchID_flat"])

    return list(IDs)


#print("By CUI: "+str(get_stitch_ID_by_CUI("C0085166")))



def get_stitch_ID_by_side_effects1(liste_name):
    IDs=[]
    for name in liste_name:
        with open('../Data/Medra/meddra_all_se.tsv', 'r') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter='\t')
            for row in tsv_reader:
                if row["Side_Effect_Name"] == name:
                    if row["Stitch_ID_flat"] not in IDs:
                        IDs.append(row["Stitch_ID_flat"])

    return IDs



def create_two_Index():
    #Index meddra_all_indications.tsv
    schema = Schema(StytchID=TEXT(stored=True), CUI=TEXT(stored=True), ConceptName=TEXT(stored=True))
    # Creating a directory for the index
    if not os.path.exists("../Meddra_all_indication"):
        os.mkdir("../Meddra_all_indication")
    ix = create_in("../Meddra_all_indication", schema)
    writer = ix.writer()
    with open('../Data/Medra/meddra_all_indications.tsv', 'r') as tsv_file:
        tsv_reader = csv.DictReader(tsv_file, delimiter='\t')
        for row in tsv_reader:
            writer.add_document(StytchID=row["StitchID_flat"], CUI=row["CUI"],ConceptName=row["ConceptName"])
    writer.commit()

    #Index meddra_all_se.tsv
    schema = Schema(StytchID=TEXT(stored=True), Side_Effect_Name=TEXT(stored=True))
    # Creating a directory for the index
    if not os.path.exists("../Meddra_all_se"):
        os.mkdir("../Meddra_all_se")
    ix = create_in("../Meddra_all_se", schema)
    writer = ix.writer()
    with open('../Data/Medra/meddra_all_se.tsv', 'r') as tsv_file:
        tsv_reader = csv.DictReader(tsv_file, delimiter='\t')
        for row in tsv_reader:
            writer.add_document(StytchID=row["Stitch_ID_flat"], Side_Effect_Name=row["Side_Effect_Name"])
    writer.commit()

#create_two_Index()
#print("By SE: "+str(get_stitch_ID_by_side_effects("Cryptosporidiosis infection")))


def get_stitch_ID_by_CUI(liste_CUI):
    res = []

    # Ouvrir l'index et créer le searcher et le parser en dehors de la boucle for
    ix = index.open_dir("../Meddra_all_indication")
    searcher = ix.searcher()
    parser = QueryParser("CUI", ix.schema)

    for CUI in liste_CUI:
        query = parser.parse(CUI)
        results = searcher.search(query, limit=None)

        for k in range(len(results)):
            res.append(results[k]['StytchID'])

    return res




def get_stitch_ID_by_side_effects(liste_SE):
    res = []

    # Ouvrir l'index et créer le searcher et le parser en dehors de la boucle for
    ix = index.open_dir("../Meddra_all_se")
    searcher = ix.searcher()
    parser = QueryParser("Side_Effect_Name", ix.schema)

    for SE in liste_SE:
        query = parser.parse(SE)
        results = searcher.search(query, limit=None)

        for k in range(len(results)):
            res.append(results[k]['StytchID'])

    return res




def getMaladiebyCUI(liste_CUI):
    ix = index.open_dir("../Meddra_all_indication")
    searcher = ix.searcher()
    parser = QueryParser("CUI", ix.schema)

    res = []

    for CUI in liste_CUI:
        query = parser.parse(CUI)
        results = searcher.search(query, limit=None)
        res.extend([(result['ConceptName'], "From meddra_all_indications.tsv") for result in results])

    res = list(set(res))

    searcher.close()

    return res


def getStitchIDbyMaladie(liste_maladie):
    res = []

    # Ouvrir l'index et créer le searcher et le parser en dehors de la boucle for
    ix = index.open_dir("../Meddra_all_indication")
    searcher = ix.searcher()
    parser = QueryParser("ConceptName", ix.schema)

    for maladie in liste_maladie:
        query = parser.parse(maladie)
        results = searcher.search(query, limit=None)

        for k in range(len(results)):
            res.append(results[k]['StytchID'])

    return res



