#-*- coding: utf-8 -*-
# dans cet exemple, la seule fonction que nous utilisons 
# du module 'os' est 'remove' 
import os 

import os.path

nom_fichier = "D:\\FUN\\Py_Fondamentaux\\Py_Fondamentaux_W4\\file3.txt"

# au départ le fichier n'existe pas
print 'Début: existence de', nom_fichier, os.path.exists(nom_fichier)
# on le crée
with open(nom_fichier,'w') as output:
    output.write('0123456789\n')
# il doit exister maintenant
print 'Milieu: existence de', nom_fichier, os.path.exists(nom_fichier)
# regardons sa taille -- 11 caratères (avec la fin de ligne)
print 'taille', os.path.getsize(nom_fichier)
# et sa date de modification 
mtime_timestamp = os.path.getmtime(nom_fichier)
print 'date de dernière modification (1)', mtime_timestamp
# pour l'afficher d'une manière un peu plus lisible
from datetime import datetime
mtime_datetime = datetime.fromtimestamp(mtime_timestamp)
print 'date de dernière modification (2)', mtime_datetime

# on le détruit
os.remove(nom_fichier)
# vérifions qu'il n'est plus là
print 'Fin: existence de', nom_fichier, os.path.exists(nom_fichier)


import glob

# ici on recherche  tous les fichiers .json dans le répertoire data/
for json in glob.glob("data/*.json"):
    print json