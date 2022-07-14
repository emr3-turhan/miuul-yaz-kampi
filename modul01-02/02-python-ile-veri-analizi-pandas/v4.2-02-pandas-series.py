################################################################################
# Pandas Series
################################################################################

# Pandas Series'i oluşturmak için pandas.Series() fonksiyonunu kullanırız.
# Ama önce Pandas kütüphanesini import edilmelidir.
import pandas as pd

# Yazımı bu şekildedir.
pd.Series([10, 77, 12, 4, 5])

# Yazdıralım
print(pd.Series([10, 77, 12, 4, 5]))

# Değişkene tanımlayalım.
s = pd.Series([10, 77, 12, 4, 5])


# Veri yapısına bakalım.
print(type(s))

# Pandas serisinin index yapısına bakalım.
print(s.index)

# Serinin içeriğindeki değerlerin veri türüne bakalım.
print(s.dtype)

# Serinin içeriğindeki değerlerin sayısal değerleri bakalım.
print(s.values)

# Burada dikkat edilmesi gereken bir şey var. Pandas serisinin değerlerine baktığımızda 'values' metodu Numpy array döndürür.
print(type(s.values))
# Bunun sebebi indexlerle değil değerlerle ilgilendiğimiz içindir.


# Pandas serisinin ilk elemanlarını görmek istediğimizde:
print(s.head()) # Pandas serisinin ilk 5 elemanını gösterir. (varsayılan 5)

# head() metodunun içerisine değer girersek ('head(n)') ilk n elemanını gösterir.
print(s.head(3)) # Pandas serisinin ilk 3 elemanını gösterir.

# Sondan elemanları görmek istediğimizde:
print(s.tail()) # Pandas serisinin son 5 elemanını gösterir. (varsayılan 5)

# tail() metodunun içerisine değer girersek ('tail(n)') son n elemanını gösterir.
print(s.tail(3)) # Pandas serisinin son 3 elemanını gösterir.



