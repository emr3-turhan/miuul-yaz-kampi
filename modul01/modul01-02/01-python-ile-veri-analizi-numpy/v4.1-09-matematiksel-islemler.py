################################################################################    
# Matematiksel İşlemler (Mathematical Operations)
################################################################################
import numpy as np

v= np.array([1,2,3,4,5])

print(v / 5)
print(v * 5 / 10)
print(v ** 2)
print(v - 1)

# Bu işlemleri metodlar aracılığı ile de yapabiliriz.
print(np.subtract(v, 1))
print(np.add(v, 1))
print(np.mean(v))
print(np.sum(v))
print(np.min(v))
print(np.max(v))
print(np.var(v))

########################
# Numpy İle İki Bilinmeyenli Denklem Çözümü
########################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

# Birinci ve ikinci denklemin katsayılarını vektör olarak tanımlayalım. (Tek satırdan oluşan arraylere vektör denir.)
a = np.array([[5,1],[1,3]])

# Denklemlerin çözümünü vektör olarak tanımlayalım.
b = np.array([12,10])

# Numpy kütüphanesinde yer alan linsolve.solve(katsayilar_array,cozumler) fonksiyonu ile denklemlerin çözümünü alabiliriz.
print(np.linalg.solve(a,b))