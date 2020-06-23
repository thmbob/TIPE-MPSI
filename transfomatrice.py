import Graphe as Gr
import cartofonds as cf

def chercheIndice(e, tab, i0=0, ifinal=-1) :
    if ifinal == -1 : ifinal = len(tab)
    for i in range(i0, ifinal) :
        if e == tab[i] : return i
    return -1

def creerGraphe(tab, c, hmin) :
    graphe = [[], []]
    for i in range(len(tab)) :
        if tab[i][2]>=hmin :
            graphe[0].append(i)
    for i in range(len(graphe[0])-1) :
        if i!=c-1 and graphe[0][i]+1 == graphe[0][i+1] :
            graphe[1].append((i, i+1))
        if graphe[0][i]+c in graphe[0]:
            graphe[1].append((i, chercheIndice(graphe[0][i]+c, graphe[0], i)))
    graphe.append(Gr.matriceAdjacente(graphe))
    return graphe

graphe = creerGraphe(cf.xyz, cf.colonnes, 1.8)

print(graphe)
for i in Gr.glouton(graphe) :
    print(i)
print(Gr.composantesConnexes(graphe))
            
