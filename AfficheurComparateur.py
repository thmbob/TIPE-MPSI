### Objectif : Programme qui permet de comparer la complexité temporelle des deux algorithmes (matrice d'adjacence et glouton) de façon expérimentale

import time
import numpy.random as rd
import matplotlib.pyplot as plt
import numpy as np

f = open('Comparateur.txt', 'r')
f.readline()
n = []      #Tableau des temps
glouton = []      #Tableau des ordres
matrice = []
for ligne in f :
    t = ligne.rstrip().split(',')
    n.append(int(t[0]))
    t = t[1].split(' ')
    glouton.append(float(t[0]))
    matrice.append(float(t[1]))

f.close()

n = np.array(n)
glouton = np.array(glouton)
matrice = np.array(matrice)

plt.plot(n, glouton**(1/2), color='blue', label='Algorithme glouton')## Glouton
plt.plot(n, matrice**(1/2), color='red', label='Algorithme des matrices')## matrice
plt.xlabel("Ordre")
plt.ylabel("Temps")
plt.legend(loc='best')

plt.show()

