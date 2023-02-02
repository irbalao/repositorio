#! /usr/bin/python
from subprocess import call
import os
import sys

cwd = str(os.getcwd())

#Creamos la variable del entorno
os.environ['GROUP_NUMBER']="44"
num_grupo= str(os.environ.get('GROUP_NUMBER'))

#Modificamos el titulo
call(['cp '+cwd+'/templates/productpage.html '+cwd+'/templates/productpage1.html'], shell=True)
copia = open( cwd + '/templates/productpage1.html', 'r')
f = open( cwd + '/templates/productpage.html', 'w')
for line in copia:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        f.write("{% block title %}" + num_grupo + "{% endblock %}")
    else:
        f.write(line)
f.close()
copia.close()
call(['rm '+cwd+'/templates/productpage1.html'],shell=True)
#Lanzamos la aplicacion
call(["python3 productpage_monolith.py 9080"], shell=True)
