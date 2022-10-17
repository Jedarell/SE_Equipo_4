import serial as s
import numpy as np

mTransicion = [[0.3, 0.5, 0.2], [0.4, 0.2, 0.4], [0.1, 0.1, 0.8]]
#mTransicion = [[round(j * 1023 / 1, 3) for j in i] for i in mTransicion]
matrizTransicion = np.array(mTransicion)


arduino = s.Serial("COM3", timeout=1, baudrate=9600)

if arduino.isOpen():
    while(True):
        cadena = arduino.readline()
        cadena = cadena.decode() #decodificacion de la cadena

        cadena = cadena.replace("\n", "")
        cadena = cadena.replace("\r", "")

        cadena = cadena.replace("E", "")
        cadena = cadena.replace("F", "")

        if cadena != "":
            print("R", cadena, "R")
            auxiliar = cadena.split("G")

            EstadosIniciales = list(map(int, auxiliar[:-1]))
            EstadosIniciales = np.array(EstadosIniciales)
            print()

            print(EstadosIniciales.dot(matrizTransicion))

# EJERCICIO: CALCULAR P1 DE LAS CADENAS QUE LEAN DESDE ARDUINO CON ESTE CODIGO
# 0 = 0; 1 = 1023



