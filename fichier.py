#-*- coding: utf-8 -*-
# iterator sur les fichiers
source = open(r'D:\FUN\Py_Fondamentaux\Py_Fondamentaux_W4\file1.txt', 'w')
for i in range(2):
    source.write("{} {}\n".format(i, i**2))
source.close()


source = open(r'D:\FUN\Py_Fondamentaux\Py_Fondamentaux_W4\file1.txt', 'r')
dest = open(r'D:\FUN\Py_Fondamentaux\Py_Fondamentaux_W4\file2.txt', 'w')
for l in source:
    dest.write(l.replace(' ', ','))
source.close()
dest.close()



