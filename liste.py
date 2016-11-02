#-*- coding: utf-8 -*-

# les comprehension de listes sont plus puissantes que les fonctions et 
[x**2 for x in range (100) if x%7 == 0]

# compréhensionn de set
# les {} sont réservés aux set et dictionnaires
{i**3 for i in range(10)}
# ou
{i**3 for i in range(100) if i%11 == 0}

# Pour la compréhension des dictionnaires
{i : i**2 for i in range(10)}

# pour un vrai usage :
# des numéro de sécu à des personnes
d = {123: 'marc', 145: 'eric', 655: 'jean'}
# d : {145: 'eric', 123: 'marc', 655: 'jean'}
#d[123] --> renvoit marc
# Comment renverser son dictionnaire et rechercher par valeur !
d2 = {d[k] : k for k in d}
# output de d2 : {'jean': 655, 'eric': 145, 'marc': 123} 
#d2['jean'] --> renvoit 655
