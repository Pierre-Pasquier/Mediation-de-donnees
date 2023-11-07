from hpo import get_id_by_disease
from hpo import get_diseases_by_symptoms
from hpo import get_disease_by_id
from OmimIndex import SearchNO
from omim_onto import NOtoCUI
from meddra import getMaladiebyCUI
from meddra import get_stitch_ID_by_CUI
from meddra import get_stitch_ID_by_side_effects
from chemsource import Search_Name
from drugbank import NomMedicamentToSE
from meddra import getStitchIDbyMaladie

def final(symptome):
    #print("aaaaaaaaaa")
    res = []

    id1 = get_diseases_by_symptoms(symptome) #liste de string
    #print("Id 1 : ", id1)

    maladie1 = get_disease_by_id(id1) #liste de string

    NO = SearchNO(symptome) #liste de string

    #print(NO)
    maladie2 = get_disease_by_id(NO) #liste de string
    #print("Maladie 2 : ", maladie2)

    CUI = NOtoCUI(NO)     #liste de string
    #print("Cui : ", CUI)

    maladie3 = getMaladiebyCUI(CUI) #liste de string
    #print("Maladie 3 : ", maladie3)


    StitchID1 = get_stitch_ID_by_CUI(CUI)    #liste de string
    #print("StitchID 1 : ", StitchID1)

    StitchID2 = get_stitch_ID_by_side_effects([symptome])  #liste de string
    #print("StitchID 2 : ", StitchID2)

    Medicament1 = Search_Name(StitchID1)     #liste de string
    #print("Médicament 1 : ", Medicament1)

    Medicament2 = Search_Name(StitchID2)     #liste de string
    #print("Médicament 2 : ", Medicament2)

    SE_Medicament1 = NomMedicamentToSE(Medicament1)  #liste de string
    #print("SE_Médicament 1 : ", SE_Medicament1)

    SE_Medicament2 = NomMedicamentToSE(Medicament2)   #liste de string
    #print("SE_Médicament 2 : ", SE_Medicament2)

    ##On cherche les médicaments soignant les symptomes des médicaments
    #NO_med1 = OmimIndex.SearchNO(SE_Medicament1)

    #CUI_med1 = omim_onto.NOtoCUI(NO_med1)

    #StitchID_med1 = meddra.get_stitch_ID_by_CUI(CUI_med1)

    #SE1_med1 = meddra.get_stitch_ID_by_side_effects(symptome)


def MaladieToMedicament(maladie):
    id = get_id_by_disease(maladie)
    CUI = NOtoCUI(id)
    StitchID = get_stitch_ID_by_CUI(CUI)

    StytchID = getStitchIDbyMaladie([maladie])

    all_stitch_ids = StitchID + StytchID
    all_stitch_ids_set = set(all_stitch_ids)
    Medicament = Search_Name(all_stitch_ids_set)

    return list(set(Medicament))


def MedicamentToMedicament(medicament, searcher, parser):
    SE = NomMedicamentToSE([medicament])
    words = SE[0].split(" ")

    all_stitch_ids = set()
    for word in words:
        no_med = SearchNO([word], searcher, parser)
        cui_med = NOtoCUI(no_med)
        stitch_id_med = get_stitch_ID_by_CUI(cui_med)
        all_stitch_ids.update(stitch_id_med)

    medicament = Search_Name(all_stitch_ids)

    return list(set(medicament))



