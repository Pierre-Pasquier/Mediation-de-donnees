import sqlite3
import re
import obonet
import networkx as nx

graph = obonet.read_obo("../Data/HPO/hpo.obo")

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

            term_ids = set()  # Utiliser un ensemble pour éviter les doublons
            for key, value in graph.nodes(data=True):
                # Check if the name or synonym matches the regex pattern
                if regex_pattern.search(value["name"]) or any(regex_pattern.search(synonym) for synonym in value.get("synonym", [])):
                    term_ids.add(key)
                    # Add alt_id(s) if available
                    for alt_id in value.get("alt_id", []):
                        term_ids.add(alt_id)

            # Find disease_ids directly linked to term_ids (without predecessors)
            disease_ids = set(term_id for term_id in term_ids if graph.in_degree(term_id) == 0)

            all_disease_ids.append(disease_ids)

    # Find the intersection of all disease ID sets
    common_disease_ids = set.intersection(*all_disease_ids)

    return list(common_disease_ids)


#name = 'Macro*'
#is_a = get_diseases_by_symptoms(name)
#print(f"Le champ 'is_a' correspondant à '{name}' est '{is_a}'")



def get_disease_by_id(id_list):
    res = []
    for id in id_list:
        con = sqlite3.connect("../Data/HPO/hpo_annotations.sqlite")
        cur = con.cursor()
        cur.execute("""SELECT disease_label FROM  phenotype_annotation WHERE sign_id = ?;""",("HP:0" + id,))
        maladies = cur.fetchall()
        res += maladies
    return res


def get_id_by_disease(disease):
    con = sqlite3.connect("../Data/HPO/hpo_annotations.sqlite")
    cur = con.cursor()
    cur.execute("""SELECT sign_id FROM  phenotype_annotation WHERE disease_label = ?;""",(disease,))
    id = cur.fetchall()[4:]
    return id

"""def test():
    final = []
    for id in get_diseases_by_symptoms(name):
        maladie = get_disease_by_id(id)
        if maladie != None:
            for element in maladie:
                if element not in final:
                    final.append(element)

    print(len(final))
    for x in final:
        print(str(x[0]))"""



