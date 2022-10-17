import numpy as np

'''
m1 = [[0.3, 0.5, 0.2], [0.4, 0.2, 0.4], [0.1, 0.1, 0.8]]
m2 = [0.1, 0.2, 0.7]

m1 = np.array(m1)
m2 = np.array(m2)

print(m1)
print(m2)

print(m1 * m2)
'''


mTransicion = [[0.3, 0.5, 0.2], [0.4, 0.2, 0.4], [0.1, 0.1, 0.8]]

#mTransicion = [[j + 1 for j in i] for i in mTransicion]
mTransicion = np.array(mTransicion)
eini = np.array([384, 337, 306])

print(eini.dot(mTransicion))
#[280.6 290.  456.4]