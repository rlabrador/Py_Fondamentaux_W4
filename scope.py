#-*- coding: utf-8 -*-


a, b = 1, 1


###
L = 10

def f():
    global L 
    L = 11

print L

f()

print L


## Modification la variable globale par la directive globale
# une  directive globale est une directive au compilateur (pour la génération du bind code - )'
# Si la génération du bond code, l'interpreteur detective si global L est premier dans la fonction

# il faut éviter d'utiliser de toute façon les variables globales
# il faut donc faire gaffe au scope --> espace de nommage
#ex:
x = 100
def f(x):
    return  x + 10 
x = f(x)
print x

