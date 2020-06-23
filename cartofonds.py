import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D 

# 1) On récupère les données
# 2) On triangulise les données
def triangulise(l, c) :
    triangles = []
    for i in range(l-1) :
        for j in range(c-1) :
            triangles.append([i*c+j, i*c+(j+1), (i+1)*c+j])
            triangles.append([(i+1)*c+j, i*c+(j+1), (i+1)*c+(j+1)])
    return triangles

xyz = np.array([[0,0,1.1], [0,1,1.2], [0,2,1.4], [0,3,1.5], [0,4,1.7], [0,5,1.8], [0,6,1.8], [0,7,1.9], [0,8,1.9], [0,9,2.0],
	        [1,0,1.2], [1,1,1.3], [1,2,1.4], [1,3,1.6], [1,4,1.5], [1,5,1.6], [1,6,1.7], [1,7,1.8], [1,8,1.9], [1,9,1.9],
	        [2,0,1.4], [2,1,1.5], [2,2,1.5], [2,3,1.7], [2,4,1.7], [2,5,1.8], [2,6,1.8], [2,7,1.7], [2,8,1.9], [2,9,2.0],
	        [3,0,1.5], [3,1,1.6], [3,2,1.6], [3,3,1.5], [3,4,1.7], [3,5,1.8], [3,6,2.0], [3,7,1.8], [3,8,1.9], [3,9,2.1],
	        [4,0,1.4], [4,1,1.5], [4,2,1.6], [4,3,1.6], [4,4,1.7], [4,5,1.9], [4,6,1.9], [4,7,1.9], [4,8,1.9], [4,9,1.9],
	        [5,0,1.5], [5,1,1.6], [5,2,1.6], [5,3,1.7], [5,4,1.8], [5,5,2.0], [5,6,1.9], [5,7,2.0], [5,8,1.9], [5,9,2.0],
	        [6,0,1.7], [6,1,1.7], [6,2,1.8], [6,3,1.7], [6,4,1.8], [6,5,2.0], [6,6,2.0], [6,7,2.1], [6,8,2.0], [6,9,2.1],
	        [7,0,1.7], [7,1,1.8], [7,2,2.0], [7,3,1.9], [7,4,1.8], [7,5,2.1], [7,6,2.3], [7,7,2.2], [7,8,2.1], [7,9,2.2],
	        [8,0,1.8], [8,1,1.9], [8,2,2.0], [8,3,1.8], [8,4,1.8], [8,5,1.9], [8,6,2.2], [8,7,1.9], [8,8,2.1], [8,9,2.1],
	        [9,0,1.7], [9,1,1.8], [9,2,1.9], [9,3,1.8], [9,4,1.8], [9,5,1.8], [9,6,2.0], [9,7,1.9], [9,8,2.0], [9,9,2.0],
                [10,0,1.8], [10,1,1.8], [10,2,1.8], [10,3,1.7], [10,4,1.7], [10,5,1.8], [10,6,1.8], [10,7,1.9], [10,8,1.9], [10,9,2.0], 
	        [11,0,1.8], [11,1,1.8], [11,2,1.7], [11,3,1.6], [11,4,1.6], [11,5,1.6], [11,6,1.7], [11,7,1.8], [11,8,1.8], [11,9,1.9],
	        [12,0,1.8], [12,1,1.8], [12,2,1.5], [12,3,1.7], [12,4,1.7], [12,5,1.8], [12,6,1.8], [12,7,1.7], [12,8,1.7], [12,9,1.8],
	        [13,0,1.7], [13,1,1.6], [13,2,1.6], [13,3,1.5], [13,4,1.7], [13,5,1.8], [13,6,2.0], [13,7,1.8], [13,8,1.7], [13,9,1.6],
	        [14,0,1.6], [14,1,1.5], [14,2,1.6], [14,3,1.6], [14,4,1.7], [14,5,1.9], [14,6,1.9], [14,7,1.9], [14,8,1.7], [14,9,1.5],
	        [15,0,1.8], [15,1,1.6], [15,2,1.6], [15,3,1.7], [15,4,1.8], [15,5,2.0], [15,6,1.8], [15,7,1.7], [15,8,1.6], [15,9,1.4],
	        [16,0,1.9], [16,1,1.7], [16,2,1.8], [16,3,1.7], [16,4,1.8], [16,5,1.8], [16,6,1.7], [16,7,1.6], [16,8,1.5], [16,9,1.3],
	        [17,0,1.7], [17,1,1.8], [17,2,2.0], [17,3,1.9], [17,4,1.8], [17,5,1.8], [17,6,1.5], [17,7,1.4], [17,8,1.4], [17,9,1.2],
	        [18,0,1.8], [18,1,1.9], [18,2,2.0], [18,3,1.8], [18,4,1.9], [18,5,1.8], [18,6,1.6], [18,7,1.5], [18,8,1.4], [18,9,1.3],
	        [19,0,1.7], [19,1,1.9], [19,2,1.9], [19,3,1.8], [19,4,1.8], [19,5,1.7], [19,6,1.6], [19,7,1.4], [19,8,1.4], [19,9,1.5],
                ])
colonnes, lignes = 10, 20
x, y, z = xyz[:,0], xyz[:,1], xyz[:,2]

triangles = triangulise(lignes,colonnes)
triangu = mtri.Triangulation(x, y, triangles=triangles)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(triangu, z, cmap='summer')
plt.show()


#2
A = (0.9, 1.3)

#3
#M est un point (un couple),
#Retourne un quadruplet de points représentant un carré
def quelCarre(M) :
    c = colonnes
    x, y = M[0], M[1]
    for i in range(colonnes) :      
        for j in range(lignes) :
            if i>x and j>y :
                return ((i-1)*c + j-1), (i*c + j-1), (i*c + j), (i-1)*c + j

print(quelCarre(A))

#M est un point (un couple),
#Retourne un triplet de points représentant un triangle
def quelTriangle(M) :
    C = quelCarre(M)
    x, y = M[0]-C[0]/colonnes, M[1]-C[0]%colonnes        #Remise à 0 des axes
    if x+y <= 1 :                       #Thm de Pythagore-Gurvan
        return (C[0], C[1], C[3])
    else :
        return (C[1], C[2], C[3])

print(quelTriangle(A))
    

#4
#M est un point (un couple), T est un triangle (triplets de points,
#Retourne un triplet de points représentant les coordonnees barycentriques dans le traingle T
def coordBarycentrique(M, T) :
    ux, uy = M[0]-T[0]/colonnes, M[1]-T[0]%colonnes
    vx, vy = M[0]-T[1]/colonnes, M[1]-T[1]%colonnes
    wx, wy = M[0]-T[2]/colonnes, M[1]-T[2]%colonnes      #On récupère les distances entre le point M et les points du triangle

    c = (-uy + ((vy - uy)/(vx - ux))*ux) / ((wy - uy) - ((vy - uy)/(vx - ux))*(wx - ux))                       #c = (-uy*vx + 2*uy*ux - ux*vy)/(wx*vy - wx*uy - ux*vy + ux*uy)
    b = (-ux + (ux - wx)*c) / (vx - ux)
    a = 1 - b - c

    return (a, b, c)

print(coordBarycentrique(A, quelTriangle(A)))


def hauteur(M) :
    T = quelTriangle(M)
    coo = coordBarycentrique(M, T)
    return (coo[0]*z[T[0]] + coo[1]*z[T[1]] + coo[2]*z[T[2]], T)

T = hauteur(A)[1]
print('\n', A, '\n', hauteur(A)[0], '\n', xyz[T[0]], xyz[T[1]], xyz[T[2]])
