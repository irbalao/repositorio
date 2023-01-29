#!/usr/bin/python3
import json
import os
import logging
from os import close
import sys
from subprocess import call

def modifHTML():
  #se pone el if para que cuando no exista variable de entrono no aparezca None
  #if os.environ.get('GROUP_NUMBER')== None:
   # return
  #else:
  h=open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r+")
  aux=open("practica_creativa2/bookinfo/src/productpage/templates/auxiliar.html", "w+")
  for line in h:
    if ("{} block title {}Simple Bookstore App{} endblock {}".format('{%', '%}', '{%', '%}')) in line:
      print("Hay una linea que es igual a la elegida")
      aux.write("{} block title {} Simple Bookstore App {} {} endblock {}".format('{%', '%}', os.environ.get('GROUP_NUMBER'), '{%', '%}'))
    else:
      aux.write(line)
  h.close()
  aux.close()
  h=open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "w+")
  aux=open("practica_creativa2/bookinfo/src/productpage/templates/auxiliar.html", "r")
  for line in aux:
    h.write(line)

#------------------------------------------------------MAIN---------------------------------------------------
def funcion(): 
  os.environ['GROUP_NUMBER']="Equipo 44"
  os.system("printenv GROUP_NUMBER")
  call(["sudo", "rm", "-r", "CDPS_P2"] )
  call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"] )
  call(["sudo", "apt-get", "-y", "install", "python"] )
  call(["sudo", "apt-get", "update"] )
  call(["sudo", "apt-get", "-y", "install", "python3-pip"] )
  os.system("pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt")
  modifHTML()
  os.system("python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080")

funcion()
