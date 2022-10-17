def euclidiana(a, b):
    distancia = 0
    for i in range(len(a)):
        distancia += (a[i] - b[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia


# CARGAR INSTANCIA
archivo = open("Instancia.txt", "r") # abre el archivo
contenido = archivo.readlines() # lee todas las lineas del archivo

# VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo completo: ') # impreso línea a línea
for l in contenido:
    print(l, end="") # por el formato en que se lee el archivo se quita el terminador (salto de línea) para evitar un doble salto
print("\n\n")

# CREA UNA LISTA EN LA QUE CADA ELEMENTO SEA UNA LINEA DEL ARCHIVO CONVERTIDA EN LISTA SEPARADA POR TABULADOR
lista = [linea.split("\t") for linea in contenido]

# VISUALIZA LISTA PROCESADA
print("Lista de lista separada por el tabulador: ")
# Impreso línea a línea
for l in lista:
    print(l)
print("\n\n")

# CONVIERTE LA LISTA DE LISTAS EN LA INSTACIA NECEARIA PARA TARBAJAR CON EL KNN
instancia = [[list(map(int, x[:7])), x[7].replace("\n", "")] for x in lista]

# VISUALIZA EL CONTENIDO DEL ARCHIVO
print("Instancia Procesada: ")
# impreso línea a línea
for l in instancia:
    print(l)
print("\n\n")

########################################################################################################################
# SELECCION / CREACION DEL VECTOR A CLASIFICAR
import serial

NC = [] # NC: No Clasificado
arduino = serial.Serial("COM3", timeout=1, baudrate=9600)

if arduino.isOpen():
    while(True):
        cadena = arduino.readline()
        cadena = cadena.decode()
        cadena = cadena.replace("\n", "")
        cadena = cadena.replace("\r", "")
        cadena = cadena[1:-2]

        if cadena != "":
            NC = cadena.split("A")
            print(NC)
            NC = list(map(int, NC))

NC = [round(i * 100 / 1023)for i in NC]

########################################################################################################################
# DEFINIR EL VALOR DE "K" - Un número entre 1 y el total de registros en la instancia
K = 15

estructuraDatos = {}

for NoCaso, registro in enumerate(instancia): # por cada elemento/registro de la instancia
    distancia_NC_i = euclidiana(NC, registro[0]) # registro[0] = vecotr carac  -- registro[1] = clase
    estructuraDatos[NoCaso] = distancia_NC_i

# VISUALIZA EL CONTENIDO DE LA ESTRUCTURA DE DATOS (TABLA DE DISTANCIAS)
print("TABLA DE DISTANCIAS: ")
#Impreso línea a línea
for key in estructuraDatos:
    print("Registro", key, " - Distancia con NC: ", estructuraDatos[key])
print("\n\n")

ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1], reverse=False) # 0 = NoCaso  1 = Distancia --> retorna una lista de tuplas

#VISUALIZA EL CONTENIDO DE LA ESTRUCTURA DE DATOS (TABLA DE DISTANCIAS) ORDENADA
print("TABLA DE DISTANCIAS ORDENADA: ")
# impreso línea a línea
for r in ordenado:
    print("Registro ", r[0], " - Distancia con NC: ", r[1])
print("\n\n")

temporalK = []
for i in range(K):
    NumDeRegistro = ordenado[i][0] # NumDeCaso
    registro = instancia[NumDeRegistro]
    temporalK.append(registro[1]) # clase/eitqueta asociada al "NumDeRegistro"

print("Clases de los K registros más parecidos(cercanos): ")
# impreso línea a línea
for t in temporalK:
    print(("\t", t))
print("\n\n")

# ENCONTRAR LA MODA EN TEMPORAL_K PARA ASIGNAR ESA ETIQUETA/CLASE AL VECTOR "NC"

from statistics import mode
claseModa = mode(temporalK)
print(NC)
print("Clase Asignada: ", claseModa)
print("\n\n")