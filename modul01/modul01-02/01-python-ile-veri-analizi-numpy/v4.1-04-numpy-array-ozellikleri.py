###############################################################################
# Numpy Array 
###############################################################################
import numpy as np

# ndim: boyut sırası
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

# Numpy array tanımlaması
a = np.random.randint(10,size=5)

# Yazdıralım
print(a)

# Arrayin boyut bilgisi (Kaç boyutlu?)
print(a.ndim)

# Arrayin şekil bilgisi (Kaç satır/sütun?)
print(a.shape)

# Arrayin eleman sayısı
print(a.size)

# Arrayin veri tipi
print(a.dtype)