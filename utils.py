from random import randint, seed
from math import sqrt

def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


def fitness(mat, repr):
    fit=0
    for i in range(len(repr)):
        fit+=mat[repr[i]][repr[i-1]]
    return fit

def distanta_pct (pct1,pct2):
    return sqrt((pct2[0] - pct1[0])**2 + (pct2[1] - pct1[1])**2)


def citeste():
    f = open ("berlin52.txt" ,"r")
    nr = int(f.readline())
    g = open ("berlin.txt", "w")

    mat=[[0]*nr for _ in range(nr)]
    coordonate = []

    for x in range(nr):
        l = f.readline()
        el = l.split(" ")
        coordonate.append((float(el[1]), float(el[2])))

    for x in range(nr):
        for y in range(nr):
            if x!=y:
                mat[x][y]=distanta_pct(coordonate[x],coordonate[y])

    g.writelines(str(nr) + "\n")
    for el in mat:
        l=""
        for x in el:
            l += str(x)
            l += " "
        l += "\n"
        g.writelines(l)
    g.close()
    f.close()


citeste()