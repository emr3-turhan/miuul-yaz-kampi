###############################################################################
# NUMPY ("Numerical Python")
###############################################################################

# Neden Numpy? (Why Numpy?) ("Daha az çaba daha fazla işlem") ("Hız")
# Numpy Array'i Oluşturmak (Creating Numpy Arrays) ("Verimli veri saklama,vektörel işlemler,fixed type 'sabit tip'")
# Numpy Array Özellikleri (Attributes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index ("Çooook önemli ve muazzam bir şey =D")
# Numpy' da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# Amaç bu iki listenin elemanlarını birbiriyle çarpmak. Normalde bu iki liste birbiriyle çarpılmak istediğimizde boş bir
# liste oluşturup bu iki listenin elemanlarını gezmemiz gerekeyiyor.


# Boş liste
ab = []


# Gezmek için döngü (klasik yol)
for i in range(0, len(a)):
    ab.append(a[i] * b[i])


# Yazdıralım
print(ab)


# Numpy ile
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

print(a * b)

