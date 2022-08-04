###############################################################################
# Numpy Array'i Oluşturmak (Creating Numpy Arrays)
###############################################################################
import numpy as np

print(np.array([1, 2, 3, 4, 5]))


# Numpy arrayin type' ına bakmak istersek
print(type(np.array([1, 2, 3, 4, 5])))


# Sıfırlardan oluşan numpy array oluşturma | "np.zeros(eleman_sayisi,dtype=data_turu)"
np.zeros(10,dtype=int)
print(np.zeros(10,dtype=int))


# Belirli bir aralıkta numpy array oluşturma | "np.random.randint(baslangic_araligi, bitis_araligi, size=eleman_sayisi)"
np.random.randint(0, 10, size = 10)
print(np.random.randint(0, 10, size = 10))

# Normal dağılıma göre numpy array oluşturma | "np.random.normal(kitle_ortalamasi, arguman, boyut)"
np.random.normal(10, 4, (3,4))
print(np.random.normal(10, 4, (3,4)))


# Genelde sıfırdan numpy array oluşturulup kullanılmaz.
# Veri setimizdeki değerleri temsil etmek için kullnılır.