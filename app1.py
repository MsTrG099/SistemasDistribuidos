#!/usr/bin/env python3

import numpy as np

# Clase 02 de Numpy

# print('---------------------------------------------')
# print('Tema')
# print('---------------------------------------------')

# a = np.array([1,2,3,4,5])
# print(a.shape)
# print('El elemento extraído del índice 2 es = ',a[2])

# print('---------------------------------------------')

# b = np.array([[1,2,3],[11,22,33]])
# print(b.shape)
# print(b)
# print('El elemento extraído de la fila 1 y la columna 2 es = ',b[1,2])

# print('---------------------------------------------')

print('---------------------------------------------')
print('ZERO / Matrix')
print('---------------------------------------------')

# Crear matriz de ceros
c = np.zeros((5, 4))
print('Matriz de 0:')
print(c)

print('---------------------------------------------')

# Crear matriz de unos
d = np.ones((3, 4))
print('Matriz de 1:')
print(d)

print('---------------------------------------------')

# Crear matriz con el valor 8
e = np.full((3, 4), 8)
print('Matriz de valor 8:')
print(e)

print('---------------------------------------------')
print('Práctica')

# Crear matriz con valores aleatorios entre 1 y 10
f = np.random.randint(1, 11, (5, 5))
print('Matriz de valores aleatorios del 1 al 10:')
print(f)

print('---------------------------------------------')

# Crear matriz con números aleatorios entre 0 y 1
print("Matriz G:")
g = np.random.random((5, 5))
print(g)

print('---------------------------------------------')

print("Matriz identidad:")
h = np.eye(10)
print(h)

print('---------------------------------------------')

# Crear submatriz
print("SubMatriz:")
f = np.random.randint(1, 21, size= (3, 4))  # Genera una matriz de enteros aleatorios entre 1 y 20
print(f)

print('---------------------------------------------')

# Extraer submatriz
m = f[:2, :2]
print(m)

print('---------------------------------------------')

n = np.random.randint(1, 101, size= (7, 5))
print (n)

print('---------------------------------------------')

# p = n[4:6,2:4]
# print (p)
# 0,0
# 6,0
# 6,4
# 0,5


print('---------------------------------------------')

h=n[[0,6,6,0],[0,0,4,4]]
print(h)
print (type(h))
print (h.shape)
print (h.ndim)

print('---------------------------------------------')

p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(p)
b=np.array([0,2,0,1])
a=np.arange(4)
# print (a)
print ('----------------------------------------------')
print (np.arange(4),b)
p [a,b]+=100
print (p)

