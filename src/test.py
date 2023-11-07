f = open("../Data/OMIM/omim.txt", "r")
lines = f.readlines()
for k in range(500):
    if lines[k] == "\n" :
        print("aaaaaaa")