###############################################################################
# Index Seçimi (Index Selection)
###############################################################################
import numpy as np

# Numpy array tanımlaması
a = np.random.randint(10, size=10)

print(a)
print(a[0])

print(a[0:5])

# Bu şekilde değer ataması yapılabilir
a[0] = 999


# Numpy array tanımlaması
m = np.random.randint(10, size=(3, 5))

print(m)

# 0. satırın 0. sütunundaki değeri alır (index kurallarını dikkat alarak)
print(m[0, 0])

# 1. satırın 1. sütunundaki değeri alır (index kurallarını dikkat alarak)
print(m[1, 1])

# 2. satırın 3. sütunundaki değeri alır (index kurallarını dikkat alarak)
print(m[2, 3])


m[2,3] = 999

# Numpy arrayler sabit veri tipine sahip olduğu için float değerler integer olarak görünür.
m[2,3] = 2.9

# Yazdırıp görelim
print(m)

print(m[:,0])
print(m[1,:])

print(m[0:2,0:3])
