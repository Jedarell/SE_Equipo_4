import serial as sr


def euclidiana(a, b):
    distancia = 0
    for i in range(len(a)):
        distancia = (a[i] - b[i]) ** 2
    distancia *= (1/2)
    distancia = round(distancia, 2)
    return distancia


# instancia: [[[CARACTERISTICAS], CLASE],... [[CARACTERISTICAS], CLASE]]
archivo = open("Instancia.txt", "r")
instancia = archivo.readlines()
instancia = [registro.split("\t") for registro in instancia]
instancia = [[list(map(int, r[:7])), r[7].replace("\n", "")] for r in instancia]

# LECTURA DEL REGISTRO(s) NC(No Clasificado) POR ARDUINO

arduino = sr.Serial("COM3", timeout=1, baudrate=9600)

NC = []
if arduino.isOpen():
    while(True):
        cadena = arduino.readline()
        cadena = cadena.decode()
        cadena = cadena.replace("\n", "")
        cadena = cadena.replace("\r", "")
        cadena = cadena[1:-2]
        if cadena != "":
            NC = cadena.split("A")
            NC = list(map(int, NC))
            break

NC = [round(i * 100 / 1023) for i in NC]

# DICCIONARIO DE DISTANCIAS A SUS RESPECTIVOS CASOS KEY: NO_CASO VALUE: DISTANCIA
estructuraDatos = {}
for no_caso, caso in enumerate(instancia):
    distancia_caso = euclidiana(NC, caso[0])
    estructuraDatos[no_caso] = distancia_caso

# ORDENAMIENTO DE LAS DISTANCIAS POR EL VALOR DE LAS DISTANCIAS - MENOR A MAYOR
ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1], reverse=False)

# K VALORES MÁS CERCANOS
k = 15
temp_k = []
for i in range(k):
    num_de_caso = ordenado[i][0]
    caso = instancia[num_de_caso]
    temp_k.append(caso[1])

# ENCONTRAR LA MODA PARA ASIGNAR CLASE AL VECTOR NC
from statistics import mode
claseModa = mode(temp_k)
NC = [NC, claseModa]
print(NC)


