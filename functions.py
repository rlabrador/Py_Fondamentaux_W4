#-*- coding: utf-8 -*-

def f(a, b, c):
    print a, b, c

#les objets passés aux fonctions sont des objets passés en référence

#exemple :
L = []
def h(a):
    a.append(1)


# on peut avoir plusieurs return dans une fonction
def f(a, b, c):
    if  b < 10:
        return a
    else:
        return c

def f(a):
    func(a)

#
def func(a):
    print a

#une fonction est polymorphe si elle accpete des paramètres de type différents

def f(a, b):
    return a + b



# positionnement des arugments d'une fonction"
# en premier les arguments nommés et les arguments avec valeur par défaut
 def f(*t):
     print f
f(1, 2, 5, 'a')
# retourne (1, 2, 5, 'a') sur f'


# déclarer une fonction alors meme que je connais pas les argugments à l'avance
# C'est la forme double étoile
#ex: 
def f(**d):
    print d

f(nom = 'coucou', prenom = 'caca', tel = '320143243')

f retourne le dictionnaire
# {'nom' : 'coucou', 'prenom' : 'caca', 'tel'' : '320143243')


# les arguments nommés peuvent avoir aussi une forme double étoiles grace à un parametre en dictionnaire
# les clés du dicitonnaires d ci-dessous passé doivent etre dans l'ordre des parametres attendus par la fonction'
#Exemple :
def f(a, b):
    print a, b

d = {'a' : 1, 'b' : 2}

f(**d)


