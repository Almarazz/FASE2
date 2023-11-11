import numpy as np


lista_de_listas = [[2,0], [3,0], [3,1], [5,0], [5,1], [5,2]]
print(lista_de_listas)
print()
a = np.array([[2,0], [3,0], [3,1], [5,0], [5,1], [5,2]])
print("El contenido del array de numpy es: ")
print(a)

print(f"Y es un objeto de tipo {type(a)}")

#Acceso a particiones de un arreglo bidimensional de numpy
a[:,0] = 15
print(a)
print()
a[:,1] = 30
print(a)


#Creación de un arreglo con todos sus elementos establecidos en ceros

arreglo2 = np.zeros(shape= (2,4), dtype = int)
print(arreglo2)
print(f"\nLas dimensiones del arreglo son {arreglo2.shape}")


#Creación de un arreglo unidimensional con valores aleatorios

arreglo_aleatorio = np.random.randint(1,11, size=10)
print(arreglo_aleatorio)


#Creación de una matriz bidimensional con valores aleatorios

matriz_aleatorio = np.random.randint(1,11, size=(2,4))
print(matriz_aleatorio)


#Creación de un arreglo que contenga una secuencia monotónica

dos_en_dos = np.arange(10,25,2)      #Cifras espaciadas de dos en dos
print(dos_en_dos)

print(f"\nLas dimensiones de la estrucutra resultante son: {dos_en_dos.shape}")


#Una lista puede contener elementos de diferentes tipos

lista = [10, "abc", 20]
print(lista)
print(*[type(elemento) for elemento in lista], sep="\n")


#Un arreglo buscará homolgar los tipos de datos

arreglo = np.array([10, "abc", 20])
print(arreglo)
print(*[type(elemento) for elemento in arreglo], sep="\n")


#Las listas no soportan la multpiplicacion matricial 

lista = [10, 15, 20, 25]
print(lista)
print(f"\n{lista * 2}")


#Al ser los arreglos de numpy equivalentes a matrices unidimensionales, SI soportan la multiplicacion

arreglo = np.array([10, 15, 20, 25])
print(arreglo)
print()
print(arreglo * 2)


#Dos matrices compatibles como arreglos de numpy SI soportan la multiplicacion.

#matriz_aleatoria = np.random.randint(1,11, size (2,4))

matrizA = np.random.randint(1,300, size=(5,10))
matrizB = np.random.randint(1,300, size=(5,10))

print(f"matriz A\n{matrizA}")
print("\nX\n")
print(f"matriz B\n{matrizB}")
print("\n=\n")
print(matrizA * matrizB)
