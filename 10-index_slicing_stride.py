numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# -----------------------
# INDEX: acceder a elementos individuales
# -----------------------
print(numeros[0])   # primer elemento -> 0
print(numeros[5])   # sexto elemento -> 5
print(numeros[-1])  # último elemento -> 9
print(numeros[-3])  # antepenúltimo -> 7

# -----------------------
# SLICING: obtener sublistas [inicio:fin]
# -----------------------
print(numeros[0:5])   # elementos 0 a 4 -> [0,1,2,3,4]
print(numeros[5:10])  # elementos 5 a 9 -> [5,6,7,8,9]
print(numeros[:4])    # desde inicio hasta índice 3 -> [0,1,2,3]
print(numeros[6:])    # desde índice 6 hasta el final -> [6,7,8,9]

# -----------------------
# STRIDE: saltos entre elementos [inicio:fin:paso]
# -----------------------
print(numeros[::2])   # cada 2 elementos -> [0,2,4,6,8]
print(numeros[1::2])  # cada 2 elementos empezando desde 1 -> [1,3,5,7,9]
print(numeros[::-1])  # invertir la lista -> [9,8,7,6,5,4,3,2,1,0]
print(numeros[5:0:-1]) # elementos de 5 a 1 en orden inverso -> [5,4,3,2,1]
