#Objet de type ensemble :

class Set :
    def __init__(self) :
        self.__set = []

    def copy(self) :
        R = Set()
        R.__set = self.__set.copy()
        return R

    def __equal__(self, E) :
        return self.__set == E.__set

    def __str__(self) :
        return str(self.__set)

    def __iter__(self) :
        return iter(self.__set)

    def __next__(self):
        pass

    def cardinal(self) :
        return len(self.__set)

    def append(self, e) :
        if e not in self :
            self.__set.append(e)

    def remove(self, e) :
        indice = -1
        for i in range(len(self.__set)) :
            if self.__set[i] == e : indice = i
        if indice != -1 :
            del self.__set[indice]

    def estVide(self) :
        return self == Set()
        


def union(A, B) :
    E = A.copy()
    for e in B :
        E.append(e)
    return E

def inter(A, B) :
    E = Set()
    for e in A :
        if e in B :
            E.append(e)
    return E

def inclu(A, B) :
    for e in A :
        if e not in B :
            return False
    return True

def prive(E, A) :
    if not inclu(A, E) :
        return Set()
    R = Set()
    for e in E :
        if e not in A :
            R.append(e)
    return R
                    
'''        
E = Set()
for i in range(40) :
    E.append(i)

print(E, E.cardinal())

A = E.copy()

print(A==E)
for i in range(10) :
    E.remove(i*5)
    E.remove(i*6)
    E.remove(i*8)

for i in range(10) :
    A.remove(i*5)
    A.remove(i*9)
    A.remove(i*13)
    A.remove(i*17)

for i in range(10) :
    A.append(i*6)

print(E)
print(A)
print(A==E)
print(union(A,E))
print(inter(E,A))
print(inclu(A,E), inclu(E,A), inclu(inter(A,E), A), inclu(E, inter(E,A)), inclu(union(E,A), E), inclu(E, union(A,E)))
'''
