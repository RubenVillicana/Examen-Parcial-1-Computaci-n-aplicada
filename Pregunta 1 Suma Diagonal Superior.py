# Examen Parcial 1
# José Rubén Villicaña Ibargüengoytia
# A01654347
# Pregunta 1

import numpy as np
import math
import sympy


# Paso 1) Solicite al usuario la dimensión  𝑚  de una matriz, mayor o igual a 3
m_int = 0

while m_int <= 2:                                        #Se coloca While para asegurar que es mayor a 3
  m = input("Introduzca la dimensión de la matriz A (≥ 3): ") #Devuelve numero entero
  m_int = int(m)

  
# Paso 2) Generar la matriz con numeros primos
lista_primos= []
size_primos = 0
total_primos = m_int*m_int
i = 2
j = 1

while size_primos < total_primos:
  a = sympy.isprime(i)
  
  if a == True:
    lista_primos.append(i)

  size_primos=len(lista_primos)
  i += 1

  
# Paso 3) Generación de la matriz
matriz_primos =[]
k = 0

for i in range(m_int):
  fila = []
  for j in range(m_int):
    fila.append(lista_primos[k])
    k += 1
  matriz_primos.append(fila)

  
# Paso 4)  Matriz de forma estructurada
print('\n')
print("La matriz A de números primos consecutivos es:")
print('\n')

join = ''

for i in range(m_int):
  for j in range(m_int):
    join += str(matriz_primos[i][j]) + '\t'
  print(join)
  join = ''

  
# Paso 5) Resolver la suma
print('\n')
print("La suma de los elementos en la matriz diagonal superior es:")
print('\n')

sum = 0
s = -1

for i in range(m_int):
  s += 1
  for j in range(s,m_int,1):
    sum = sum + matriz_primos[i][j]

print(sum)
