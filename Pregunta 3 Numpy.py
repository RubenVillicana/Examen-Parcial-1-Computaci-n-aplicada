# Examen Parcial 1
# José Rubén Villicaña Ibargüengoytia
# A01654347
# Pregunta 3 (numpy)

import numpy as np

# Obtener los valores de la matriz
A = np.array([[0.25, 0.15, 0.00], [0.45,0.50,0.75], [0.30,0.35,0.25]])
B = np.array([1.5, 5, 3])

# Calcular el valor de las incognitas
x = np.linalg.solve(A, B)

# Imprimir
print("La solucion del sistema de ecuaciones es la siguiente:")
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])