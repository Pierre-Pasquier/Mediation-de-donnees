############################################################################################################
#                       Stych - ATC
############################################################################################################


#
# # Compte le nombre de ligne totale du fichier chemical.sources.v5.0.tsv
#
# f = open("./Data/STITCH - ATC/chemical.sources.v5.0.tsv", "r")
# lines = f.readline()
# k = 0
# while lines:
#     k += 1
#     lines = f.readline()
#
# print("Le nombre de ligne est"+str(k))
#
# # # Compte le nombre de ligne du fichier chemical.sources.v5.0.tsv qui contient ATC
# #
# # f = open("./Data/STITCH - ATC/chemical.sources.v5.0.tsv", "r")
# # lines = f.readline()
# # k = 0
# # while lines:
# #     if "ATC" in lines:
# #         k += 1
# #     lines = f.readline()
# #
# # print("Le nombre de ligne est"+str(k))
# #

# Compte le nombre de code ATC dans le fichier chemical.sources.v5.0.tsv qui correspond à un stytchID

# Sortie :
# Le nombre de ligne est263085321
# Le nombre de ligne est3387

############################################################################################################

#Trouver les stytchID qui ont un ATC

import csv

import OmimIndex
import chemsource
import hpo
# IDs=[]
# with open('../Data/Medra/meddra_all_se.tsv', 'r') as tsv_file:
#     tsv_reader = csv.DictReader(tsv_file, delimiter='\t')
#     k = 0
#     stack = "a"
#     for row in tsv_reader:
#         if row["Stitch_ID_flat"] != stack:
#             print("bip")
#             stack = row["Stitch_ID_flat"]
#             L = chemsource.SearchIndication_chem([row["Stitch_ID_flat"]])
#             if len(L) > 0:
#                 k += 1
#
#     print("Le nombre de stytch qui ont un ATC : "+str(k))
# String = "Adverse reactions occur at a frequency of &lt; 1/1000 and are usually mild and transient in nature. Reported adverse effects include chest pain (pleuritic/non-cardiac), fever, dyspepsia, voice alteration (hoarseness), pharyngitis, dyspnea, laryngitis, rhinitis, decreased lung function, rash, urticaria, and conjunctivitis. There is no evidence of carcinogenic or mutagenic properties. The safety of dornase alfa has not been studied in pregnant women, nursing women and children under the age of 5 years old."
# L = String.split(" ")
# for mot in L:
#     O = hpo.get_diseases_by_symptoms([mot])
#     if len(O) > 0:
#         NO_med1 = OmimIndex.SearchNO(mot)
#         print(str(NO_med1) +" " + mot)


import final

#print(final.MedicamentToMedicament("Lepirudin"))

print(final.MaladieToMedicament("Celiac disease"))



