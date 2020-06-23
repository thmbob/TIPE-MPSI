### Objectif générer des matrices de façon aléatoires et determiner si elles sont connexes

import numpy.random as rd
import matplotlib.pyplot as plt
import numpy as np
import Graphe as gr    #le fichier "Graphe.py" doit se situer dans le même dossier que ce fichier pour que le programme fonctionne

#Pour chaque noeud de la courbe, on décide avec une probabilité p si ce noeud est relié aux vosins --> Complexité quadratique
def liens(p, n) :
    matrice = rd.random((n,n))
    for i in range(n) :
        for j in range(i, n) :
            if matrice[i][j] < p :
                matrice[i][j] = 1
                matrice[j][i] = 1
            else :
                matrice[i][j] = 0
                matrice[j][i] = 0
    for i in range(n) :
        matrice[i][i] = 0

    return np.array(matrice, dtype=np.uint64)    #plus grands entier possible pour éviter les dépassements (pour les matrices de grand ordre (>50) il y aura quand même des dépassements)


k = 500            #Nombre de valeurs
p = np.linspace(0.01, 1, k)
t = 2000         #Taille des échantillons --> (plus ce nombre est grand moins il y a de perturbations dans la courbe)
for n in range(12, 31, 18) :         #Ordre du graphe --> Complexité quadratique (à partir de 10 ça devient long, au delà de 30 c'est très long et plus grand que 50 c'est turbo long)
    c = []              #Tableau utilisé pour afficher le graphique
    f = open("Dot - ordre " + str(n) + ".txt", 'w')       #fichier pour stocker les résultats afin de les réutiliser
    f.write("Ordre " + str(n) + "\n")
    for i in range(k) :
        print(str(i/k*100) + "%")
        s = 0
        for j in range(t) :             #on crée t matices avec une probabilité de liens i afin de savoir la proportion de matrices connexes en foncttion de la probabilité de liens entre les noeuds
            matAdj = liens(p[i], n)
            points = np.arange(1, n+1)      #les points sont étiquetés de 1 à n
            graphe = [points.tolist(), [], matAdj]
            graphe[1] = gr.listeArretes(graphe)
            if gr.estConnexeGlouton(graphe) :
                s += 1
        c.append(s/t)
        f.write(str(p[i]) + " " + str(s/t) + "\n")
 
    c = np.array(c)
    plt.plot(p, c, label="Ordre "+str(n))
    plt.legend(loc="upper right")
    print("Ordre : " + str(n) + " : terminé\n")

    f.close()

    
plt.xlabel("Probabilité que deux noeuds soient liés")
plt.ylabel("Probabilité que le graphe soit connexe")
plt.title("Probabilité de la connexité de graphes d'ordre " + str(n)+ " en fonction de la probabilité qu'il y ait un lien entre les noeuds")
plt.show()
