#Objectif : tracer la courbe des probabilités qu'un graphe soit connexe en fonction des probabilités que 2 noeuds soient liés
#           à partir des données stockées sur les documents textes "Connexité - ordre n.txt"

import numpy as np
import matplotlib.pyplot as plt

#ordre des graphes dont on veut la courbe :
n = 30

f = open("Connexité - Ordre 60" + ".txt", 'r')

f.readline()  #On passe la première ligne du document qui indique seulement l'ordre

x = []      #Tableau des probabilités que deux points soient liés
y = []      #Tableau des proportions de graphe connexes 
for ligne in f :
    t = ligne.rstrip().split(' ')
    x.append(float(t[0]))
    y.append(float(t[1]))

f.close()

x = np.array(x)
y = np.array(y)

plt.plot(x, y)

plt.xlabel("Probabilité que deux sommets soient liés")
plt.ylabel("Proportion de graphe connexe")
plt.title("Probabilité de la connexité de graphes d'ordre " + str(n)+ " en fonction de la probabilité qu'il y ait un lien entre les sommets")
plt.show()
    
