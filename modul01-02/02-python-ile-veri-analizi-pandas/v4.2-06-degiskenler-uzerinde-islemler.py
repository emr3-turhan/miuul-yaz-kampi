############################################################################################
# Değişlenler Üzerinde İşlemler
############################################################################################
import pandas as pd
import seaborn as sns

# Eğer veri setindeki tüm columnları göremiyorsanız.
# pd.set_option("display.max_columns", None)
# çalıştırabilirsiniz.

# Dataframe oluşturmak için. (titanic veriseti)
df = sns.load_dataset("titanic")

# Dataframe in ilk 5 satırını görmek için.
print(df.head())

# ... (burada "age") içerisinde var mı diye sormak için:
print("age" in df)

# Eğer içerisinde varsa "age" columnunu görmek için:
print(df["age"].head())

# Bu ifadenin type'ını görmek için:
print(type(df["age"].head()))
# <class 'pandas.core.series.Series'> yani Series tipindedir. 

# Eğer dataframe olarak kalmasını istiyorsanız çift parantez kullanmalısınız.
print((df[["age"]]).head())


# Bakalım
print(type((df[["age"]]).head()))
# <class 'pandas.core.frame.DataFrame'> yani DataFrame tipindedir.
# Aslnda çift parantez kullanmamızın sebebi ortada bir liste olduğu için.

# Birden fazla column'u görmek için.
print(df[["age","alive"]].head())

# Index değeri olarak liste de kullanabiliriz.
col_names = ["age","adult_male","alive"]
print(df[col_names])

# Yeni bir column eklemek istersek (burada var olan column üzerinden türetiyoruz)
df["age2"] = df["age"]**2

# Bakalım
print(df.head())

# Oluşturduğumuz yeni columndan ('age2') ve 'age' den age3 column'ını oluşturuyoruz.
df["age3"] = df["age"] / df["age2"]

# Bakalım
print(df.head())

# Bir column'ı silmek için:
print(df.drop("age2", axis=1,).head()) # Kalıcı değil kalıcı olması için inplace=True yazılır

# Daha detaylı seçim yapmak için:
print(df.loc[:, ~df.columns.str.containes("age")].head()) # ~ ile kolonlarının içinde "age" yoksa alır. Eğer ~  yı kaldırırsak içinde "age" olanları alır. 

