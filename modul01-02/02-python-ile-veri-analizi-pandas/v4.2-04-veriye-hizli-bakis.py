################################################################################
# Veriye Hızlı Bakış (Quick Look at Data)
################################################################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())

# Son değerler bakmak için.
print(df.tail())

# Dataframe şekil bilgisi.
print(df.shape)

# Dataframe detaylı bilgi almak için.
print(df.info())

# Dataframedeki değişkenlerin isimlerine erişmek için.
print(df.columns)

# Dataframedeki index bilgisine erişmek için.
print(df.index)

# Dataframe ile alakalı bazı istatistiksel verileri almak için.
print(df.describe())

# Daha okunabilir hale getirmek için traspozesini alabiliriz.
print(df.describe().T)

# Dataframede eksiklik var mı diye bakmak için.
print(df.isnull().values.any())

# DIKKAT: "df.isnull().values" ifadesi NumPy array döndürür.

# Veri setindeki degiskenlerin eksikliklerini görmek için.
print(df.isnull().sum())

# Kategorik değişkenlerin sınıflarını ve sayılarını görmek için.
print(df["sex"].value_counts())
