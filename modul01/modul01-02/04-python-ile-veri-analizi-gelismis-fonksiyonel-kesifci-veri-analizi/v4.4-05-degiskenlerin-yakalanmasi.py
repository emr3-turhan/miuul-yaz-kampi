########################################################################################################################
# Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi
######################################################################################################################

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

print(df.info())

def grab_col_names(dataframe,cat_th=10,car_th=20):
    """Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
        Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler 

    Args:
    -----
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                Numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optional
                Kategorik fakat kardinal olan değişkenler için sınıf eşik değeri
    Returns:
    --------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal olan değişken listesi

    Notes:
    -----
    cat_cols + num_cols + cat_but_cat = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.
    Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols
    
    
    
    
    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and df[col].dtypes in ["int64","float64"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > car_th and str(df[col].dtypes) in ["category","object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Gözlemler: {dataframe.shape[0]}")
    print(f"Değişkenler: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

grab_col_names(df)
