#-*- coding: utf-8 -*-
# iterator sur les fichiers
with open(r"D:\FUN\Py_Fondamentaux\Py_Fondamentaux_W4\file3.txt", "w") as source:
    for i in range(2):
        source.write("{} {}\n".format(i, i**2))


with open(r"D:\FUN\Py_Fondamentaux\Py_Fondamentaux_W4\file3.txt","r") as source:
    with open(r"D:\FUN\Py_Fondamentaux\Py_Fondamentaux_W4\file4.txt","w") as dest:
        for l in source:
            dest.write(l.replace(' ', ','))