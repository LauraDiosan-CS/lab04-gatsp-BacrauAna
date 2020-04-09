from utils import fitness
from ga import GA

def readNet(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if mat[i][j] >= 1:
                d += 1
            noEdges += mat[i][j]
        degrees.append(d)
    noEdges=noEdges//2
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net

def readFloat(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(" ")
        for j in range(n):
            mat[-1].append(float(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if mat[i][j] >= 1:
                d += 1
            noEdges += mat[i][j]
        degrees.append(d)
    noEdges=noEdges//2
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net



def GAmenu():
    param={}
    print("Dati numarul cromozomilor:")
    popSize=input()
    try:
        popSize=int(popSize)
    except TypeError:
        popSize=50
    param['popSize']=popSize

    print("Dati numarul generatiilor:")
    noGen = input()
    try:
        noGen = int(noGen)
    except TypeError:
        noGen = 50
    param['noGen'] = noGen
    # print("Evolutia folosita este SteadyState")
    param['FuncEvolutie'] = 'oneGenerationSteadyState'
    # param['FuncEvolutie'] = 'oneGenerationElitism'
    # param['FuncEvolutie'] = 'oneGeneration'
    return param

def GAplay(ga):
    allBestFitnesses = []
    alBestPath=[]
    generations = []
    ga.initialisation()
    ga.evaluation()
    bestGen=0
    currentBestChromo=ga.bestChromosome()

    for g in range(ga.getGAparam()['noGen']):
        bestChromo= ga.bestChromosome()
        if bestChromo.fitness < currentBestChromo.fitness:
            currentBestChromo=bestChromo
            bestGen=g
        bestSolX = bestChromo.repres
        alBestPath.append(bestSolX)

        bestSolY = bestChromo.fitness
        allBestFitnesses.append(bestSolY)

        generations.append(g)

        # alg logic
        print("Generatia: ", g, "--> Drumul: ",alBestPath[g], "--> fitness-ul:", allBestFitnesses[g])
        getattr(ga,ga.getGAparam()['FuncEvolutie'])()

    print("Cea mai buna cale --> ", currentBestChromo.repres, "cu fitness-ul --> ", currentBestChromo.fitness, "in generatia --> ", bestGen)

    # comunitatiDetectate=currentBestChromo.componente()
    # print("Numarul comunitatilor identificate:",max(comunitatiDetectate),
    #       "\nComunitatile detectate: ",comunitatiDetectate,
    #       "\nFitness: ",currentBestChromo.fitness,
    #       "\nIn generatia: ",bestGen)


    # A = np.matrix(ga.getProbParam()['retea']['mat'])
    # G = nx.from_numpy_matrix(A)
    # pos = nx.spring_layout(G)  # compute graph layout
    # plt.figure(figsize=(7, 7))
    # nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
    # nx.draw_networkx_edges(G, pos, alpha=0.3)
    # plt.show(G)

def main():
    while True:
        print("1 --> Easy1\n2 --> Easy2\n3 --> Easy3\n4 --> Medium\n5 --> Hard\n6 -->Berlin\nx --> Iesire\nCmd: ")
        comanda=input()
        if comanda=="x":
            break
        elif comanda=="1":
            retea=readNet("easy.txt")
            paramProbl = {'min': 0, 'max': retea['noNodes'] - 1, 'function': fitness, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA=GAmenu()
            obiectGA=GA(paramGA,paramProbl)
            GAplay(obiectGA)
        elif comanda=="2":
            retea = readNet("easy2.txt")
            paramProbl = {'min': 0, 'max': retea['noNodes'] - 1, 'function': fitness, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA = GAmenu()
            obiectGA = GA(paramGA, paramProbl)
            GAplay(obiectGA)
        elif comanda == "3":
            retea = readNet("easy3.txt")
            paramProbl = {'min': 0, 'max': retea['noNodes'] - 1, 'function': fitness, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA = GAmenu()
            obiectGA = GA(paramGA, paramProbl)
            GAplay(obiectGA)
        elif comanda=="4":
            retea = readNet("medium.txt")
            paramProbl = {'min': 0, 'max': retea['noNodes'] - 1, 'function': fitness, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA = GAmenu()
            obiectGA = GA(paramGA, paramProbl)
            GAplay(obiectGA)
        elif comanda=="5":
            retea = readFloat("hard.txt")
            paramProbl = {'min': 0, 'max': retea['noNodes'] - 1, 'function': fitness, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA = GAmenu()
            obiectGA = GA(paramGA, paramProbl)
            GAplay(obiectGA)
        elif comanda=="6":
            retea = readFloat("berlin.txt")
            paramProbl = {'min': 0, 'max': retea['noNodes'] - 1, 'function': fitness, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA = GAmenu()
            obiectGA = GA(paramGA, paramProbl)
            GAplay(obiectGA)


main()