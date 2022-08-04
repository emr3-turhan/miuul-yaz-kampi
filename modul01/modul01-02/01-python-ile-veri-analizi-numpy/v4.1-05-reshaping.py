###############################################################################
# Yeniden Şekillendirme (Reshaping)
###############################################################################
import numpy as np

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

# Numpy array tanımlaması
ar = np.random.randint(1, 10, size=9)
ar.reshape(3,3)

# 9 elemanlı bir arraye 3x3 şeklinde yeniden şekillendirme yapılabilir.
reshaped = ar.reshape(3,3)

#Yazdıralım
print(reshaped)



