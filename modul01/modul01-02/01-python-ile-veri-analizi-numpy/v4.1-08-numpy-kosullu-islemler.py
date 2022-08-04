################################################################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
################################################################################
import numpy as np
v = np.array([1,2,3,4,5])

########################
# Klasik Döngü İle
########################

ab = []

for i in v:
    if i < 3:
        ab.append(i)

########################
# Numpy İle
########################

print(v < 3)

print(v[v < 3])
print(v[v > 3])
print(v[v != 3])
print(v[v == 3])
print(v[v >= 3])

# Numpy sayesinde döngü ve koşullu ifadelerle yapacağımız işlemleri tek satırda yapabiliriz.

