############################################################################################
# Pandas'ta Secim İşlemleri (Selection in Pandas)
############################################################################################

# Kütüphaneleri import ediyoruz.
import pandas as pd
import seaborn as sns

# Dataframe oluşturmak için.
df = sns.load_dataset("titanic")

# Dataframe in ilk 5 satırını görmek için.
print(df.head())

# Index değerlerine erişmek için.
print(df.index)

# İlk elemanın silinmiş halini görmek için. (kalıcı değil!!!)
print(df.drop(0,axis=0).head()) # Axis=0 satır, Axis=1 ise sütun.

# Birden fazla indexi silmek için. Fancy index kullanabiliriz. Bunun için silinecek index listesi tanımlayabiliriz.
delete_index = [1,3,5,7]

# Önceki örnekteki 0 yerine liste adını verdiğimiz zaman bu örnekteki 1,3,5,7 indexlerini siler.
print(df.drop(delete_index,axis=0).head())

# Dataframe'deki silme işlemini kalıcı olarak yapmak için.
#df=df.drop(delete_index,axis=0,)
#print(df.head())

# Veya
# df.drop(delete_index,axis=0,inplace=True)

########################
# Değişkeni Indexe Çevirmek
########################

print(df["age"].head())
# Veya
print(df.age.head())

# Indexleri değiştirmek için.
df.index = df["age"]

# Age artık index değeri olarak kullanılıyor. Yani age değişkenini silebiliriz.
df.drop("age",axis=1,inplace=True) # inplace=True değeri kalıcı olarak değiştirir.

# Yazdıralım.
print(df.head())


########################
# Indexi Değişkene Çevirmek
########################

# Birinci yol
df["age"] = df.index # Age değişkeni aslında şuan yok (sildik,yeniden oluşturulacak.).

#Yazdıralım.
print(df.head())


# İkinci yol
print(df.reset_index().head())
df = df.reset_index()
print(df.head())




