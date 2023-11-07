import time
start_time = time.time()

def NOtoCUI(liste_no):
    with open("../Data/OMIM/omim_onto.csv", "r") as f:
        lines = f.readlines()

    cui = set()

    for line in lines:
        elements = line.split(",")
        no = elements[0].split("/")[-1]

        if no in liste_no:
            cui.update(elements[-3].split('|'))

    return cui


#print("--- %s seconds ---" % (time.time() - start_time))