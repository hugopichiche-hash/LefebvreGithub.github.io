from random import *

def liste_utilisateur(n=5):
    l=[]
    for i in range(n):
       p=int(input("Quelle nombre veut tu ajouter ?"))
       l.append(p)
    return l

def liste_aleatoire(n,boremin,bornemax):
    liste=[]
    for i in range(n):
        liste.append(randint(boremin,bornemax))
    return liste


l1=liste_utilisateur(4)
print(l1)
l2=liste_aleatoire(4,0,50)
print(l2)