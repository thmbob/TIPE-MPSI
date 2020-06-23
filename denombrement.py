import numpy as np
import matplotlib.pyplot as plt

def creerTableau(l, c) :
    tab = []
    for i in range(l) :
        tab.append([])
        for j in range(c) :
            tab[i].append(0)
    return tab

def pascal(n) :
    tab = creerTableau(n+1, n+1)
    for i in range(n+1) :
        tab[i][0] = 1
    for i in range(1, n+1) :
        print(i)
        for j in range(1, i+1) :
            tab[i][j] = tab[i-1][j-1] + tab[i-1][j]
    return tab

triangle = pascal(1300)

def binom(k, n) :
    return triangle[n][k]

def denombr(n) :
    tab = creerTableau(n+1, binom(2, n)+1)
    tab[1][0]
    for i in range(1, n+1) :
        print(i)
        for j in range(i-1, binom(2,n)+1) :
            s = 0
            for k in range(1, i) :
                for a in range(j+1) :
                    s += tab[k][a] * binom(k-1, i-1) * binom(j-a, binom(2,i-k))
            tab[i][j] = binom(j, binom(2, i)) - s
    return tab

tab = denombr(30)

def C(n, k) :
    return tab[n][k]
5

def dicho(f, a, b, eps) :
    t = 0
    while b-a > eps :
        t = (a+b)/2
        if f(t)*f(a) <= 0 :
            b = t
        else :
            a = t
    return (a+b)/2


def probaConnexeTheo(x, n) :
    e = binom(2, n)
    s=0
    for a in range(0, e) :
        s += float(C(n, a)) * x**a * (1-x)**(e-a)
    return s

def calculProbaLien(p, n) :
    return dicho(lambda x: p-probaConnexeTheo(x, n), 0, 1, 0.01)

x = np.linspace(-0.001, 1., 10000)
for i in range(2, 31) :
    y = probaConnexeTheo(x, i)
    plt.plot(x, y, label='Ordre ' + str(i))
    print(i)
plt.legend()
plt.show()
