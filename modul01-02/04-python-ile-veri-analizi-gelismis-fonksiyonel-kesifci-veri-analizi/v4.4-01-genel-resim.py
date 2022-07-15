##############################################################################################
# GELİŞMİŞ FONKSİYONEL KEŞİFİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
##############################################################################################
# 1. Genel Resim
# 2. kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3. Sayısal Değişken Analizi (Analysis of Numeric Variables)
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
# 5. Korelasyon Analizi (Analysis of Correlation)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  

# Eğer veri setindeki tüm columnları göremiyorsanız.
# pd.set_option("display.max_columns", None)
# çalıştırabilirsiniz.

# Dataframe oluşturmak için. (titanic veriseti)
df = sns.load_dataset("titanic")

# Dataframe in ilk 5 satırını görmek için.
print(df.head())

# Veri setine uygulanabilecek metodların listesi:
# df.info()
# df.describe().T
# df.head()
# df.tail()
# df.columns
# df.index
# df.dtypes
# df.shape
# df.isnull().sum()
# df.isnull().values.any()

# dataframe e yapilan degisiklikleri gormek icin
def check_df(dataframe,head=5):
    print("#################### Shape #####################")
    print(dataframe.shape)
    print("#################### Types #####################")
    print(dataframe.dtypes)
    print("#################### Head #####################")
    print(dataframe.head(head))
    print("#################### Tail #####################")
    print(dataframe.tail(head))
    print("#################### NA #####################")
    print(dataframe.isnull().sum())
    print("#################### Quantiles #####################")
    print(dataframe.describe([0,0.05,0.50,0.95,0.99,1]).T)


check_df(df)

df = sns.load_dataset("tips")
check_df(df)