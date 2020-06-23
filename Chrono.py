import Graphe as G
import time
import numpy.random as rd
import matplotlib.pyplot as plt
import numpy as np

'''n = 10  #Nombre de graphe à tester
v = 1000  '''#Nombre de points

def liens(p, v) :
    matrice = rd.random((v,v))
    for i in range(v) :
        for j in range(i, v) :
            if matrice[i][j] < p :
                matrice[i][j] = 1
                matrice[j][i] = 1
            else :
                matrice[i][j] = 0
                matrice[j][i] = 0
    for i in range(v) :
        matrice[i][i] = 0

    return np.array(matrice, np.uint64)

f = open("Compare5000 p variable.txt", 'w')
f. write("Ordre,Glouton Matrice\n")

p = np.linspace(0.0001, 0.01, 5)
n = 5
for v in range(1, 1202, 100) :
    f.write(str(v) + ",")
    print(v)

    graphes = []
    for i in range(n) :
        matAdj = liens(p[i], v)
        points = np.arange(1, v+1)      #les points sont étiquetés de 1 à n
        graphe = [points.tolist(), [], matAdj]
        graphe = G.listeArretes(graphe)
        graphes.append(graphe)

    t1 = time.time()
    for i in range(n) :
        G.estConnexeGlouton(graphes[i])
    t2 = time.time()

    t3= time.time()
    for i in range(n) :
        G.estConnexe(graphes[i])
    t4 = time.time()

    f.write(str(20*(t2-t1)) + ' ' + str(20*(t4-t3)) + '\n')

f.close()
