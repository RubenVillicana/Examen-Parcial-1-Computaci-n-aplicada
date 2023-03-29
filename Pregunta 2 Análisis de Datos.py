# Examen Parcial 1
# José Rubén Villicaña Ibargüengoytia
# A01654347
# Pregunta 2

import numpy as np
import math
import csv
import statistics

from matplotlib import pyplot as plt
from scipy.stats import norm
from sklearn.linear_model import LinearRegression

# Paso 1) Importar los datos de excel a Python

with open('Respuestas.csv', mode='r') as csv_file:
  csv_reader = csv.reader(csv_file)

  estatura = []
  calzado = []
  sexo =[]
  
  for row in csv_reader:
    estatura.append(row[1]) #Obtener los valores de estatura 
    calzado.append(row[2]) #Obtener los valores de calzado
    sexo.append(row[3]) #Obtener los valores de sexo

  estatura.pop(0) #Elimina el primer valor de la lista
  calzado.pop(0)
  sexo.pop(0)

  estatura = list(map(int, estatura))  #Pasar los datos de string a int
  calzado = list(map(float, calzado))  ##Pasar los datos de string a float
  indices = list(range(1, 222))

  
#Paso 2) Obtener la Media
mean_estatura = statistics.mean(estatura)
mean_calzado = statistics.mean(calzado)

print("La media de los datos de estatura es:",mean_estatura)
print("La media de los datos de calzado es:",mean_calzado)
print("\n")


#Paso 3) Obtener la desviacion estandar
sd_estatura = np.std(estatura)
sd_calzado = np.std(calzado)

print("La desviacion estandar de los datos de estatura es:",sd_estatura)
print("La desviacion estandar de los datos de calzado es:",sd_calzado)


#Paso 4) Encontrar la función gaussiana
min_estatura = min(estatura)
max_estatura = max(estatura)

x_estatura = np.linspace(min_estatura, max_estatura, 1000)
y_estatura = norm.pdf(x_estatura, mean_estatura, sd_estatura)

min_calzado = min(calzado)
max_calzado = max(calzado)

x_calzado= np.linspace(min_calzado, max_calzado, 1000)
y_calzado = norm.pdf(x_calzado, mean_calzado, sd_calzado)


#Paso 5) Graficar histograma y Gausiana
  #a) Estatura
    #Histograma
clases = 20
rango = (104,189)
plt.figure(1)
plt.title("Histograma: Estatura")
plt.xlabel("Clases")
plt.hist(estatura, range=rango, bins = clases, density=False)
plt.show()

    #Gausiana 
plt.figure(2)
plt.title("Función Gaussiana: Estatura")
plt.plot(x_estatura, y_estatura)
plt.show()


  #b) Calzado
clases = 20
rango = (22.5,30)
plt.figure(3)
plt.title("Histograma: Calzado")
plt.xlabel("Clases")
plt.hist(calzado, range=rango, bins = clases, density=False)
plt.show()

    #Gausiana 
plt.figure(4)
plt.title("Función Gaussiana: Calzado")
plt.plot(x_calzado, y_calzado)
plt.show()


#Paso 6) Encontrar la probabilidad dentro de la primer desviacion estandar
print("\n")
#Probabilidad estatura
z_e_1 = (mean_estatura - sd_estatura)
z_e_2 = (mean_estatura + sd_estatura)
p_e_1 = norm.cdf(z_e_1,loc=mean_estatura, scale=sd_estatura)
p_e_2 = norm.cdf(z_e_2,loc=mean_estatura, scale=sd_estatura)
p_e = p_e_2-p_e_1

print("La probabilidad de caer dentro de la primer desviación de la estatura es de: ", p_e)

#Probabilidad calzado
z_c_1 = (mean_calzado- sd_calzado)
z_c_2 = (mean_calzado + sd_calzado)
p_c_1 = norm.cdf(z_c_1,loc=mean_calzado, scale=sd_calzado)
p_c_2 = norm.cdf(z_c_2,loc=mean_calzado, scale=sd_calzado)
p_c = p_c_2-p_c_1

print("La probabilidad de caer dentro de la primer desviación del calzado es de: ", p_c)

#Paso 7) Regresion Lineal
  #General
print("\n")
print("Regresion Lineal: General")
x = np.array(estatura).reshape((-1,1))
y = np.array(calzado)
model = LinearRegression()
model.fit(x,y)
model = LinearRegression().fit(x,y)
print("m: ",model.coef_)
print("b: ",model.intercept_)
r_sq = model.score(x, y)
y_pred = model.predict(x)
print("R^2: ",r_sq)

plt.figure(5)
plt.scatter(x, y, color='black')
plt.plot(x, y_pred, color='blue')
plt.title('Relación entre Estatura y Tamaño de Calzado: General')
plt.xlabel('Estatura')
plt.ylabel('Tamaño de Calzado')
plt.show()

  #Masculino
Masculino_estatura = []
Masculino_calzado = []
for i in range(len(sexo)):
  a = sexo[i]
  b = 'Masculino'
  if(a==b):
    Masculino_estatura.append(estatura[i])
    Masculino_calzado.append(calzado[i])

print("\n")
print("Regresion Lineal: Masculino")
x = np.array(Masculino_estatura).reshape((-1,1))
y = np.array(Masculino_calzado)
model = LinearRegression()
model.fit(x,y)
model = LinearRegression().fit(x,y)
print("m: ",model.coef_)
print("b: ",model.intercept_)
r_sq = model.score(x, y)
y_pred = model.predict(x)
print("R^2: ",r_sq)

plt.figure(6)
plt.scatter(x, y, color='black')
plt.plot(x, y_pred, color='blue')
plt.title('Relación entre Estatura y Tamaño de Calzado: Masculino')
plt.xlabel('Estatura Masculina')
plt.ylabel('Tamaño de Calzado Masculino')
plt.show()


  #Femenino
Femenino_estatura = []
Femenino_calzado = []
for i in range(len(sexo)):
  a = sexo[i]
  b = 'Femenino'
  if(a==b):
    Femenino_estatura.append(estatura[i])
    Femenino_calzado.append(calzado[i])

print("\n")
print("Regresion Lineal: Femenino")
x = np.array(Femenino_estatura).reshape((-1,1))
y = np.array(Femenino_calzado)
model = LinearRegression()
model.fit(x,y)
model = LinearRegression().fit(x,y)
print("m: ",model.coef_)
print("b: ",model.intercept_)
r_sq = model.score(x, y)
y_pred = model.predict(x)
print("R^2: ",r_sq)

plt.figure(7)
plt.scatter(x, y, color='black')
plt.plot(x, y_pred, color='blue')
plt.title('Relación entre Estatura y Tamaño de Calzado: Femenino')
plt.xlabel('Estatura Femenina')
plt.ylabel('Tamaño de Calzado Femenino')
plt.show()

  #Prefiero no decirlo (No se puede hacer la regresion lineal ya que solo es 1 dato)
Otro_estatura = []
Otro_calzado = []
for i in range(len(sexo)):
  a = sexo[i]
  b = 'Prefiero no decirlo'
  if(a==b):
    Otro_estatura.append(estatura[i])
    Otro_calzado.append(calzado[i])

print("\n")
print("Regresion Lineal: Prefiero no decirlo")
x = np.array(Otro_estatura).reshape((-1,1))
y = np.array(Otro_calzado)
#model = LinearRegression()
#model.fit(x,y)
#model = LinearRegression().fit(x,y)
#print("m: ",model.coef_)
#print("b: ",model.intercept_)
#r_sq = model.score(x, y)
#y_pred = model.predict(x)
#print("R^2: ",r_sq)

plt.figure(8)
plt.scatter(x, y, color='blue')
#plt.plot(x, y_pred, color='red')
plt.title('Relación entre Estatura y Tamaño de Calzado: Otro')
plt.xlabel('Estatura Otro')
plt.ylabel('Tamaño de Calzado Otro')
plt.show()