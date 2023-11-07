import time
start_time = time.time()


f = open("../Data/OMIM/omim.txt","r")

lines = f.readlines()

symptome = "Jaundice"

l = []
k=0
while k < len(lines):
    if lines[k][:10] == "*FIELD* CS":
        k+=1
        while lines[k][0] != "*" :
            if lines[k][-1] != ":" and symptome in lines[k]:
                while lines[k][:10] != "*FIELD* NO":
                    k+=1
                l.append(lines[k+1][:-1])
            k+=1
    k+=1

print(l)
print(len(l))
print("--- %s seconds ---" % (time.time() - start_time))






