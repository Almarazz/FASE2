import numpy as np


arreglo_uni = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

#Identificar aquellos valores del arreglo menores a 5
filtro = arreglo_uni < 5
print(filtro)

resultado = arreglo_uni[filtro]
print()
print(resultado)


#Demostración de filtrado booleano sobre un arreglo bidimensaional

matriz_ejemplo = np.random.randint(1,300, size=(2,5))
print(matriz_ejemplo)
print()

filtro = matriz_ejemplo > 100
print(filtro)
print()

resultado = matriz_ejemplo[filtro]
print(resultado)


#Demostración del cálculo de estadisticos descriptivos sobre un arreglo unidimensional de numpy

datos = np.random.randint(1,200, size=(18,))
print("Los datos son: ")
print(datos)

#Por metodos directo del arreglo
minimo = datos.min()
maximo = datos.max()

print(f"\nLos datos tienen un rango de {maximo - minimo}. abarcando desde el {minimo} hasta el {maximo}")


#Por metodos de libreria

minimo = np.amin(datos)
maximo = np.amax(datos)

print(f"\nLos datos tienen un rango de {maximo - minimo}. abarcando desde el {minimo} hasta el {maximo}")

primer_cuartil = np.percentile(datos, 25)
mediana = np.median(datos)
tercer_cuartil = np.percentile(datos, 75)

print(f"\nLa mediana de los datos es igual a {mediana}")
print(f"\nEl primer cuartil es igual a {primer_cuartil}, mientras que el tercer cuartil es igual a {tercer_cuartil}")
print(f"\nCon rango intercuartil = {primer_cuartil} a {tercer_cuartil} o {tercer_cuartil - primer_cuartil}")


#Por metodos directo del arreglo

media = datos.mean()
desviacion_estandar = datos.std()
varianza = datos.var()

#Por legibilidad, formateamos a cuatro posiciones despues del punto decimal
print(f"\nLos datos poseen una media aritmetica de {media:.4f}, con una varianza de {varianza:.4f} y una desviacion estandar de {desviacion_estandar:.4f}")


#Por metodos de la libreria
media = np.mean(datos)
desviacion_estandar = np.std(datos)
varianza = np.var(datos)
print(f"\nLos datos poseen una media aritmetica de {media:.4f}, con una varianza de {varianza:.4f} y una desviacion estandar de {desviacion_estandar:.4f}")
