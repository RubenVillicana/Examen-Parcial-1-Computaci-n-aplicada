# Examen Parcial 1
# José Rubén Villicaña Ibargüengoytia
# A01654347
# Pregunta 3

import numpy as np
import math

#Paso 1) Obtener los valores de la matriz
A = [[0.25, 0.15, 0.00], [0.45,0.50,0.75], [0.30,0.35,0.25]]
B = [[1.50], [5.00], [3.00]]

#Paso 2) Calcular el detrminante del denominador
det_Denominador = (A[0][0]*A[1][1]*A[2][2])+(A[0][1]*A[1][2]*A[2][0])+(A[0][2]*A[1][0]*A[2][1])-(A[0][1]*A[1][0]*A[2][2])-(A[0][0]*A[1][2]*A[2][1])-(A[0][2]*A[1][1]*A[2][0])

print("Determinante del denominador: ",det_Denominador)
print("\n")

#Paso 3) Calcular el detrminante de las incognitas
det_x1 = (B[0][0]*A[1][1]*A[2][2])+(A[0][1]*A[1][2]*B[2][0])+(A[0][2]*B[1][0]*A[2][1])-(A[0][1]*B[1][0]*A[2][2])-(B[0][0]*A[1][2]*A[2][1])-(A[0][2]*A[1][1]*B[2][0])

print("Determinante del numerador x1: ",det_x1)
print("\n")

det_x2 = (A[0][0]*B[1][0]*A[2][2])+(B[0][0]*A[1][2]*A[2][0])+(A[0][2]*A[1][0]*B[2][0])-(B[0][0]*A[1][0]*A[2][2])-(A[0][0]*A[1][2]*B[2][0])-(A[0][2]*B[1][0]*A[2][0])

print("Determinante del numerador x2: ",det_x2)
print("\n")

det_x3 =(A[0][0]*A[1][1]*B[2][0])+(A[0][1]*B[1][0]*A[2][0])+(B[0][0]*A[1][0]*A[2][1])-(A[0][1]*A[1][0]*B[2][0])-(A[0][0]*B[1][0]*A[2][1])-(B[0][0]*A[1][1]*A[2][0])

print("Determinante del numerador x3: ",det_x3)
print("\n")

#Paso 4) Calcular el valor de las incognitas
x1 = det_x1/det_Denominador
x2 = det_x2/det_Denominador
x3 = det_x3/det_Denominador

print("Cantidad de Fetrtilizante de potacio: ",x1)
print("Cantidad de Fetrtilizante de nitrato: ",x2)
print("Cantidad de Fetrtilizante de fosfato: ",x3)