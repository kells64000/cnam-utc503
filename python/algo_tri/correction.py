## version habituelle avec le modulo, non demandée ici.
def estPair0(n):
    return n % 2 == 0


##print(estPair0(14))
##print(not estPair0(15))
##print(estPair0(0))

def estImpair0(n):
    return n % 2 != 0


##print(not estImpair0(14))
##print(estImpair0(15))
##print(not estImpair0(0))

##écriture déclarative à passer en impératif avec Python
##estPair(0)
##not estPair(1)
##estPair(n) = n>1, estImpair(n-1)

## Autres méthodes d'affichage non demandées ici
def afficherNombresPairs(n):
    for i in range(n):  ## i allant de 0 à n-1
        if estPair0(i):
            print(i)


##afficherNombresPairs(10)

def afficherNombresPairs2(n):
    for i in range(0, n, 2):  ## i allant de 0 à n-1 par pas de 2
        print(i)


##afficherNombresPairs2(10)


## CE QUI ÉTAIT DEMANDÉ, nombres positifs ou négatifs,
def estPair(n):
    return ((n >= 0) and ((n == 0) or estImpair(n - 1))) \
           or ((n < 0) and estImpair(n + 1))


def estImpair(n):
    return ((n > 0) and ((n == 1) or estPair(n - 1))) \
           or ((n < 0) and estPair(n + 1))


##Une autre façon de traiter les nombres négatifs en s'appuyant sur le 3e pilier
##pour écrire une fonction récursive : comment initialiser le traitement ?

def estPairAux(n):
    return (n >= 0) and ((n == 0) or estImpairAux(n - 1))


def estImpairAux(n):
    return (n == 1) or estPairAux(n - 1)


def estPair(n):
    if n < 0:
        n = 0 - n
    return estPairAux(n)


def estImpair(n):
    if n < 0:
        n = 0 - n
    return estImpairAux(n)


##print(estPair(52))
##print(not estImpair(52))
##print(not estPair(5))
##print(estImpair(5))
##print(estPair(-52))
##print(not estPair(-5))
##print(not estImpair(-52))
##print(estImpair(-5))
##print(estPair(0))
##print(not estPair(1))
##print(not estImpair(0))
##print(estImpair(-1))

## extraireMinimum supprime et retourne le plus petit de la liste
def extraireMinimum(liste):
    if liste != []:
        petit = liste[0]
        for elem in liste:
            if elem < petit:
                petit = elem

        liste.remove(petit)
        return petit
    ##else implicite qui ne fait rien si la liste est vide -> return None


l1 = [4, 78, 5, 4, 2, 1, 3, 6, 5, 8, 9, 6, 5, 4, 8, 5, 2, 1, 3, 0]
l1Sauv = [4, 78, 5, 4, 2, 1, 3, 6, 5, 8, 9, 6, 5, 4, 8, 5, 2, 1, 3, 0]
l2 = [45]
l2Sauv = [45]
l3 = []


##print(min(l1)==extraireMinimum(l1))
####print(l1)
##print(min(l2)==extraireMinimum(l2))
####print(l2)
##print(extraireMinimum(l3)==None)

##la méthode travaille sur une copie de la liste en entrée pour éviter les effets de bord.
def triSelection(liste):
    listeTriee = []
    taille = len(liste)
    copie = list(liste)
    for i in range(taille):
        petit = extraireMinimum(copie)
        listeTriee.append(petit)
    return listeTriee


##print(triSelection(l1)==sorted(l1))
##print(l1==l1Sauv)
##print(triSelection(l2))
##print(l2==l2Sauv)
##print(triSelection(l3)==[])

##procédure qui modifie la liste en entrée
def insererTrie(elem, liste):
    i = 0
    taille = len(liste)
    fini = (i >= taille)
    while not fini:
        fini = liste[i] > elem
        if not fini:
            i += 1
            fini = (i >= taille)
    liste.insert(i, elem)


##la méthode travaille sur une copie de la liste en entrée pour éviter les effets de bord.
def triInsertion(liste):
    listeTriee = []
    taille = len(liste)
    copie = list(liste)
    for i in range(taille):
        elem = copie[0]
        insererTrie(elem, listeTriee)
        copie = copie[1:]
    return listeTriee


##print(triInsertion(l1)==sorted(l1))
##print(l1==l1Sauv)
##print(triInsertion(l2)==l2)
##print(l2==l2Sauv)
##print(triInsertion(l3)==[])

def triBulle(liste):
    copie = list(liste)
    taille = len(liste)
    for i in range(taille - 1):
        for i in range(taille - i - 1):
            if copie[i] > copie[i + 1]:
                (copie[i], copie[i + 1]) = (copie[i + 1], copie[i])
    return copie

##print(triBulle(l1)==sorted(l1))
##print(l1==l1Sauv)
##print(triBulle(l2)==l2)
##print(l2==l2Sauv)
##print(triBulle(l3)==[])

