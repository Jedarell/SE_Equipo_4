import random as rd
def euclidiana(a, b):
    dif = [(a[i] - b[i]) ** 2 for i in range(a)]
    distancia = round(sum(dif) ** 1/2)
    return distancia


archivo = open("Kmeans_instancia.txt", "r")
instancia = archivo.readlines()
instancia = [registro.split("\t") for registro in instancia]
instancia = [[list(map(float, r[:7])), r[7].replace("\n", "")]for r in instancia]

print(instancia)

centroides = []
for i in range(5):
    nuevo = rd.randint(0, len(instancia))
    ultimo =
    centroides[i] =

