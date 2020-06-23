###Objectif : Définir un ensemble de fonctions permettant de manipuler des graphes
### Le programme 1 repose sur le calcul de matrices d'adjacence su graphe en utilisant les deux propriétés suivantes :
###    (1) La matrice d'adjacence M d'un graphe élevée à la puissance k donne les chemins de longueur k entre deux sommets (M^k[i][j] est le nombre de cheemins de longueur k entre i et j
###    (2) Dans un graphe connexe à n sommets, il existe un chemin de longueur inférieur à n-1 entre deux sommets
###    Pour un graphe à n sommets, il suffit ainsi de calculer la somme des puissances de sa matrice d'adjacence (jusqu'à n-1) : si elle contient des 0 alors le graphe n'est pas connexe
### Le programme 2 est un algorithme glouton, il parcourt en profondeur le graphe pour déterminer sa connexité

import numpy as np
import numpy.linalg
import Set as S


#Une matrice sera une liste de trois objets :
#    [0] - Une liste des points, ie. une liste contenant les étiquettes de chaque point les éléments stokés ces éléments peuvent avoir n'importe quel type (int, float, string, tuple,...)
#    [1] - Une liste des arrêtes, ie une liste de couple d'indices représentant les arrêtes du graphe où chaque indice correspond à un élément de la liste des points.
#          En d'autres termes, deux points sont liés si un couple formé de leurs indices dans la liste des points se trouve dans la liste des arrêtes
#    [2] - La matrice d'adjacence du graphe (une matrice numpy)


def ordre(graphe) :             #nombre de sommets
    return len(graphe[0])


def nbrArretes(graphe) :
    return len(graphe[1])


def matriceAdjacente(graphe) :  #Retourne la matrice d'adjacence du graphe à partir de la liste des arrêtes
    arretes = graphe[1]
    matrice = np.array([np.zeros(ordre(graphe)) for i in range(ordre(graphe))])
    for a in arretes :
        matrice[a[0]][a[1]] = 1
        matrice[a[1]][a[0]] = 1

    return np.array(matrice, dtype=np.uint64)    #uint64 <=> plus grand entier possible pour éviter les dépassements


def listeArretes(graphe) :  #Retourne la liste des arrêtes du graphe à partir de sa matrice d'adjacence
    matAdj = graphe[2]
    arretes = []
    n = ordre(graphe)
    for i in range(n) :
        for j in range(i, n) :
            if matAdj[i][j] == 1 :
                arretes.append((i, j))
    return [graphe[0], arretes, graphe[2]]
    

def composantesConnexes(graphe) :   #Renvoie la liste des composantes connexes d'un graphe
    if len(graphe[2]) == 0 :
        graphe[2] = matriceAdjacente(graphe)
    matAdj = graphe[2]
    n = ordre(graphe)
    
    matChemins = np.identity(n, dtype = np.uint64)
    matMul = np.matrix(graphe[2])
    for i in range(n) :
        matChemins += matChemins*matMul
    
    composantes = []
    points = graphe[0]
    pointsNonTraites = graphe[0].copy()
    for p in range(n) :
        if points[p] in pointsNonTraites :
            composantes.append([points[p]])
            for i in range(p+1, n) :
                if matChemins[p][i] != 0 :
                    composantes[-1].append(points[i])
                    pointsNonTraites.remove(points[i])
    return composantes

def estConnexe(graphe) :
    return len(composantesConnexes(graphe)) == 1


def voisin(p, graphe) :
    matAdj = graphe[2]
    voisins = []
    for i in range(ordre(graphe)) :
        if matAdj[i][p] == 1 :
            voisins.append(i)
    return voisins

def parcours(p, graphe, visites, composante) :
    for v in voisin(p, graphe) :
        composante.append(v)
        if v not in visites :
            visites.append(v)
            parcours(v, graphe, visites, composante)


def glouton(graphe) :
    n = ordre(graphe)
    visites = []
    composantes = []
    for p in range(n) :
        if p not in visites :
            visites.append(p)
            composantes.append(S.Set())
            composantes[-1].append(p)
            parcours(p, graphe, visites, composantes[-1])
    return composantes

def estConnexeGlouton(graphe) :
    tab = glouton(graphe)
    return len(tab) == 1
        
###Code d'exemple :        
'''
graphe = [[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'], [(0, 1), (0, 2), (3, 4), (4, 5), (5, 3), (2, 7), (7, 8), (9, 7), (10, 7), (10, 8), (10, 2)], []]
graphe[2] = matriceAdjacente(graphe)
print(composantesConnexes(graphe))
composantes = glouton(graphe)
for E in composantes :
    print(E)

'''
