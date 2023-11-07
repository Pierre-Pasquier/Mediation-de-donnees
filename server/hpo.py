import sqlite3
import re
import obonet
import networkx as nx



def get_diseases_by_symptoms(symptoms):
    all_disease_ids = []
    graph = obonet.read_obo("../Data/HPO/hpo.obo")
    for symptome in symptoms:
        sub_symptoms = symptome.split(" ET ")
        for sub_symptom in sub_symptoms:
            # Replace * with .*
            user_regex_pattern = sub_symptom.replace('*', '.*')

            # Compile the regex pattern
            regex_pattern = re.compile(user_regex_pattern)

            term_ids = {key for key, value in graph.nodes(data=True) if regex_pattern.search(value["name"]) or any(regex_pattern.search(synonym) for synonym in value.get("synonym", []))}
            term_ids.update(alt_id for key, value in graph.nodes(data=True) for alt_id in value.get("alt_id", []) if key in term_ids)

            # Find disease_ids directly linked to term_ids (without predecessors)
            disease_ids = {term_id for term_id in term_ids if graph.in_degree(term_id) == 0}

            all_disease_ids.append(disease_ids)

    # Find the intersection of all disease ID sets
    common_disease_ids = set.intersection(*all_disease_ids)

    return list(common_disease_ids)



def get_disease_by_id(ids):
    with sqlite3.connect("../Data/HPO/hpo_annotations.sqlite") as con:
        cur = con.cursor()
        query = f"SELECT DISTINCT disease_label FROM phenotype_annotation WHERE sign_id IN ({','.join('?' * len(ids))})"
        cur.execute(query, ids)
        source_info = "From hpo.obo --> hpo_annotations.sqlite"
        maladies = [(disease.upper(), source_info) for row in cur.fetchall() for disease in row[0].split(";") if disease.strip()]

    return maladies

def get_id_by_disease(disease):
    con = sqlite3.connect("../Data/HPO/hpo_annotations.sqlite")
    cur = con.cursor()
    cur.execute("""SELECT sign_id FROM  phenotype_annotation WHERE disease_label = ?;""",(disease,))
    id = cur.fetchall()[4:]
    return id
