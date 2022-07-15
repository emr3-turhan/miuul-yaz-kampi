###############################################################################
# Odev-05
###############################################################################


from unicodedata import numeric
import pandas as pd
import seaborn as sns

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df = sns.load_dataset("titanic")
print(df.head())

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
print(df["sex"].value_counts())

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz
print(df.nunique())

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
print(df["pclass"].nunique())

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
print("**** pclass ****")
print(df["pclass"].value_counts())
print("**** parch ****")
print(df["parch"].value_counts())

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
print(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")


# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
print(df[df["embarked"] == "C"])

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
print(df[df["embarked"] != "S"])

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
print(df[(df["age"] < 30) & (df["sex"] == "female")])

# Görev 10: Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.
print(df[(df["fare"] > 500) | (df["age"] > 70)])

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
print(df.isnull().sum())

# Görev 12: who değişkenini dataframe’den çıkarınız.
print(df.drop("who", axis=1))

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df['deck'].fillna(df['deck'].mode()[0], inplace=True)
print(df["deck"].isnull().sum())
print(df["deck"].head())

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz
df['age'].fillna(df['age'].median(), inplace=True)
print(df["age"].isnull().sum())
print(df["age"].head())

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
print(df.groupby(["sex", "pclass"]).agg({"survived": ["sum", "count", "mean"]}))

# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
# setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
df["age_flag"] = df.apply(lambda x: 1 if x["age"] < 30 else 0, axis=1)
print(df.head())

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df = sns.load_dataset("tips")
print(df.head())

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin sum, min, max ve mean değerlerini bulunuz
print(df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]}))

# Görev 19: Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz
print(df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]}))

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre sum, min, max ve mean değerlerini bulunuz.
print(df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby(["day"]).agg({"total_bill": ["sum", "min", "max", "mean"],"tip": ["sum", "min", "max", "mean"]}))

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
print(df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean())

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
print(df.head())

# Görev 23: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz. Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit
# olanlara 1 verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
# Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate alınacktır. Parametre olarak cinsiyet ve total_bill
# alan bir fonksiyon yazarak başlayınız. (If-else koşulları içerecek)

print(df[(df["total_bill"] > 0) & (df["sex"] == "Male")]["total_bill"].mean())
print(df[(df["total_bill"] > 0) & (df["sex"] == "Female")]["total_bill"].mean())

m_f = df[(df["total_bill"] > 0) & (df["sex"] == "Male")]["total_bill"].mean()
f_f = df[(df["total_bill"] > 0) & (df["sex"] == "Female")]["total_bill"].mean()

def t_b_flag(df,sex="sex",total_bill="total_bill"):
    if df[sex] == "Female":
        if df[total_bill] < f_f:
            return 0
        return 1 # Geriye büyükler ve eşit olan durum kalıyor
    else:
        if df[total_bill] < m_f:
            return 0
        return 1

df["total_bill_flag"] = df.apply(t_b_flag, axis=1)

print(df.head())

#Görev 24: total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.
print(df.groupby("sex")["total_bill_flag"].value_counts())

# Görev25:  Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyiyeni birdataframe'eatayınız.
sdf = df.sort_values("total_bill_tip_sum", ascending=False).head(30) # ascending=False yazılırsa büyükten küçüğe sıralanır
print(sdf.shape)
print(sdf.head(30))




