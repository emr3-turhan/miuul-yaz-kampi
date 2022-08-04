################################################################################
# Pivot Table
################################################################################
import pandas as pd
import seaborn as sns

# Eğer veri setindeki tüm columnları göremiyorsanız.
# pd.set_option("display.max_columns", None)
# çalıştırabilirsiniz.

# Dataframe oluşturmak için. (titanic veriseti)
df = sns.load_dataset("titanic")

# Dataframe in ilk 5 satırını görmek için.
print(df.head()) 

# Pivot table verilerin gösterimini kolaylaştırır. Varsayılan olarak, verilen değerlerin ortalamasını alır. (mean)
print(df.pivot_table("survived","sex","embarked"))

# Varsayılanı değiştirmek için "aggfunc" argümanı eklenir.
print(print(df.pivot_table("survived","sex","embarked",aggfunc="std"))) # Şuan standart sapma hesaplayacak
# Pivot table aynı zaman da group by işlemide yapmış olur.

# İstersek farklı değişkenlere göre tekrar kırabiliriz. Örneğin:
print(df.pivot_table("survived","sex",["embarked","class"]))

# Dataframe'deki bir sayısal değişkeni kategorik değişkene çevirmek istersek 'pd.cut' veya 'pd.qcut' kullanılır.
# 'pd.cut' belirlediğimiz değer aralıklarına göre bölüp, kategorik değişken oluşturken 'pd.qcut' ise 
# çeyreklik (kartil) değerlerine göre kendi bölerek kategorik değişken oluşturur.

# Dataframe'de yeni yaş değişkeni oluşturalım.
df["new_age"] = pd.cut(df["age"], [0,10,18,25,40,90])
# Bakalım.
print(df.head())

# Yeni yaş değişkeni ile pivot table yapalım.
print(df.pivot_table("survived","sex",["new_age","class"]))