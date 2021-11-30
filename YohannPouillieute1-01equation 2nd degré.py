

import random
from math import*

a = float(input("Entrer a (différent de 0): "))
b = float(input("Entrer b: "))
c = float(input("Entrer c: "))

def calculer_delta(a,b,c):
    return b*b-4*a*c

def resoudreEquationSecondDegre(a,b):
    delta = calculer_delta(a,b,c)
    if a==0:
        a = float(input("Entrer un réel différent de 0 pour a"))
        resoudreEquationSecondDegre(a,b)
    else:
        if delta > 0:
            racineDelta=sqrt(delta)
            result1 =(-b-racineDelta)/(2*a)
            result2 =(-b+racineDelta)/(2*a)
            texte = "Les solutions de l'équation sont: {"+str(result1)+","+str(result2)+"}"
        elif delta == 0:
            result1 = -b/(2*a)
            texte = "L'équation a pour solution: {"+str(result1)+"}"
        else:
            result1 = "Aucune"
            texte = "L'équation n'a pas de solution"
        print(texte)
    
resoudreEquationSecondDegre(a,b)


