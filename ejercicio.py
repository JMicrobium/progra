"""Realice un programa que evalue la expresión:
r=(3x**2 + 6y)**(1/2)
Nota: Utilice la función sqrt de la librería math para calcular la raíz cuadrada (from math
import sqrt). La librería math también posee la función pow(a, b) que calcula a**b"""
from math import sqrt
from math import pow
X=float(input("ingrese un valor===>"))
Y=float(input("ingrese un valor===>"))
r=((3*((X)**(2))+(6*Y))**(1/2))
print(r)