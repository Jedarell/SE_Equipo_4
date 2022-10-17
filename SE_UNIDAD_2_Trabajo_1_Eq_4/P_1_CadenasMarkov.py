import numpy as n

mTransicion = [[0.3, 0.5, 0.2], [0.4, 0.2, 0.4], [0.1, 0.1, 0.8]]

mE = [0.1, 0.2, 0.7]

matrizTransicion = n.array(mTransicion)
matrizEstadosIniciales = n.array(mE)

print("matrizTransicion:", matrizTransicion)
print("\nMatriz E. Iniciales:", matrizEstadosIniciales)

'''
P1 = matrizEstadosIniciales.dot(matrizTransicion)
print("P1:", P1)

P2 = P1.dot(matrizTransicion)
print("P2:", P2)

P3 = P2.dot(matrizTransicion)
print("P3:", P3)
'''


n = int(input("Ingresa n: "))

mn = matrizEstadosIniciales.dot(matrizTransicion)

for i in range(n-1):
    mn = mn.dot(matrizTransicion)

print(mn)
