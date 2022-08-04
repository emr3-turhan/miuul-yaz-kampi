###############################################################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
###############################################################################

######################################
#İş Problemi
######################################

# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
# seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
# oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
# şirkete ortalama ne kadar kazandırabileceğini tahmin etmek
# istemektedir.


# Örneğin:
# Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek
# kullanıcının ortalama ne kadar kazandırabileceği belirlenmek
# isteniyor.


######################################
# Veri Seti Hikayesi
######################################

# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
# ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri
# seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
# tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
# kullanıcı birden fazla alışveriş yapmış olabilir.

# +-------+---------+------+---------+-----+
# | PRICE | SOURCE  | SEX  | COUNTRY | AGE |
# +-------+---------+------+---------+-----+
# |    39 | android | male |  bra    |  17 |
# |    39 | android | male |  bra    |  17 |
# |    49 | android | male |  bra    |  17 |
# |    29 | android | male |  tur    |  17 |
# |    49 | android | male |  tur    |  17 |
# +-------+---------+------+---------+-----+


######################################
# Değişkenler
######################################

# persona.csv

# PRICE – Müşterinin harcama tutarı
# SOURCE – Müşterinin bağlandığı cihaz türü
# SEX – Müşterinin cinsiyeti
# COUNTRY – Müşterinin ülkesi
# AGE – Müşterinin yaşı


######################################
# Proje Görevleri
######################################

######################################
# Kural Tabanlı Sınıflandırma
######################################

# Uygulama Öncesi Veri Seti:

# +-------+---------+------+---------+-----+
# | PRICE | SOURCE  | SEX  | COUNTRY | AGE |
# +-------+---------+------+---------+-----+
# |    39 | android | male |  bra    |  17 |
# |    39 | android | male |  bra    |  17 |
# |    49 | android | male |  bra    |  17 |
# |    29 | android | male |  tur    |  17 |
# |    49 | android | male |  tur    |  17 |
# +-------+---------+------+---------+-----+


#Hedeflenen çıktı:

# +--------------------------+---------+---------+
# |  customers_level_based   |  PRICE  | SEGMENT |
# +--------------------------+---------+---------+
# | BRA_ANDROID_FEMALE_0_18  | 35.6453 |    B    |
# | BRA_ANDROID_FEMALE_19_23 | 34.0773 |    C    |
# | BRA_ANDROID_FEMALE_24_30 | 33.8639 |    C    |
# | BRA_ANDROID_FEMALE_31_40 | 34.8983 |    B    |
# | BRA_ANDROID_FEMALE_41_66 | 36.7371 |    A    |
# +--------------------------+---------+---------+

######################################
# Görev 1: Aşağıdaki Soruları Yanıtlayınız
######################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd

df = pd.read_csv("persona.csv")

def get_view_of_df(dataframe):

    # Show the first 5 rows of the dataframe
    # head() ile ilk 5 satırı göster
    print("************* HEAD *************")
    print(dataframe.head())
    print("********************************")

    # Show the last 5 rows of the dataframe
    # Son değerler bakmak için.
    print("************* TAIL *************")
    print(dataframe.tail())
    print("********************************")

    # Show the shape info of the dataframe
    # Dataframe şekil bilgisi.
    print("************* SHAPE *************")
    print(dataframe.shape)
    print("*********************************")

    # Show the detailed info of the dataframe
    # Dataframe detaylı bilgi almak için.
    print("************* INFO *************")
    print(dataframe.info())
    print("********************************")

    # Show the column names of the dataframe
    # Dataframedeki değişkenlerin isimlerine erişmek için.
    print("************* COLUMNS *************")
    print(dataframe.columns)
    print("***********************************")

    # Show the indexes of the dataframe
    # Dataframedeki index bilgisine erişmek için.
    print("************* INDEX *************")
    print(dataframe.index)
    print("*********************************")

    # Show some statistical info of the dataframe
    # Dataframe ile alakalı bazı istatistiksel verileri almak için.
    print("************* DESCRIBE *************")
    print(dataframe.describe())
    print("************************************")

    # We can transpose the dataframe to make it easier to read
    # Daha okunabilir hale getirmek için traspozesini alabiliriz.
    print("************* TRANSPOSED DESCRIBE *************")
    print(dataframe.describe().T)
    print("***********************************************")

    # Check for null values in the dataframe
    # Dataframede eksiklik var mı diye bakmak için.
    print("************* ISNULL *************")
    print(dataframe.isnull().values.any())
    print("**********************************")

    # Show null values in variables of the dataframe
    # Veri setindeki degiskenlerin eksikliklerini görmek için.
    print("************* NULLSUM *************")
    print(dataframe.isnull().sum())
    print("***********************************")

get_view_of_df(df)
print("***********************************")


# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

# Kaç unique SOURCE vardır?
print(df["SOURCE"].nunique())
print("**************")
# Frekansları nedir?
print(df["SOURCE"].value_counts())
print("***********************************")


# Soru 3: Kaç unique PRICE vardır?

print(df["PRICE"].nunique())
print("***********************************")


# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

print(df["PRICE"].value_counts())
print("***********************************")


# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

print(df["COUNTRY"].value_counts())
print("***********************************")


# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
print(df.groupby("COUNTRY")["PRICE"].sum())
print("***********************************")


# Soru 7: SOURCE türlerine göre satış sayıları nedir?
print(df.groupby("SOURCE")["PRICE"].count())
print("***********************************")


# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
print(df.groupby("COUNTRY")["PRICE"].mean())
print("***********************************")


# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
print(df.groupby("SOURCE")["PRICE"].mean())
print("***********************************")


#  Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
print(df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean())
print("***********************************")



######################################
# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
######################################

# Kodu bu şekilde yazarsanız Görev 3 teki sıralama işlemini reset_index() kullanmadan yapamazsınız.
# print(df.groupby(["COUNTRY", "SOURCE","SEX","AGE"])["PRICE"].mean())
# print("***********************************")

# Bu şekilde reset_index() kullanmadan sıralama işlemi için kullanılabilir.
#print(df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}))

# Bunu bir dataframe yapabiliriz.
# group_df = df.groupby(["COUNTRY", "SOURCE","SEX","AGE"])["PRICE"].mean()
# group_df = group_df.reset_index()
# print(group_df)
# print("***********************************")

print(df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}))



######################################
# Görev 3: Çıktıyı PRICE’a göre sıralayınız
######################################

# • Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız
# • Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
print(agg_df)
print("***********************************")

######################################
# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
######################################

agg_df = agg_df.reset_index()
print(agg_df)
print("***********************************")


######################################
# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
######################################

# Age değişkenini kategorik değişkene çeviriyoruz.
def age_num_to_cat(dataframe,age="AGE"):
    if dataframe[age] >= 41 and dataframe[age] <= 70:
        return "41_70"
    elif dataframe[age] >= 31 and dataframe[age] < 41:
        return "31_40"
    elif dataframe[age] >= 24 and dataframe[age] < 31:
        return "24_30"
    elif dataframe[age] >= 19 and dataframe[age] < 24:
        return "19_23"
    elif dataframe[age] >= 0 and dataframe[age] < 19:
        return "0_18"
    else:
        return "out_of_range"

# Yeni "AGE_CAT" değişkeni oluşturup, agg_df’e ekliyoruz.
agg_df["AGE_CAT"] = agg_df.apply(age_num_to_cat, axis=1)

# agg_df’i görüntüleyelim.
print(agg_df)
print("***********************************")

######################################
# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
######################################

# • Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# • Yeni eklenecek değişkenin adı: customers_level_based
# • Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.

# Bu tabloda bulunan gözlemler bir araya gelecek

# +---------+---------+--------+-----+-------+---------+
# | COUNTRY | SOURCE  |  SEX   | AGE | PRICE | AGE_CAT |
# +---------+---------+--------+-----+-------+---------+
# | bra     | android | male   |  46 |  59.0 | 41_66   |
# | usa     | android | male   |  36 |  59.0 | 31_40   |
# | fra     | android | female |  24 |  59.0 | 24_30   |
# | usa     | ios     | male   |  32 |  54.0 | 31_40   |
# | deu     | ios     | female |  36 |  49.0 | 31_40   |
# +---------+---------+--------+-----+-------+---------+


# Elde edilmesi gereken çıktı

# +--------------------------+-------+
# |  customers_level_based   | PRICE |
# +--------------------------+-------+
# | BRA_ANDROID_MALE_41_66   |  59.0 |
# | USA_ANDROID_MALE_31_40   |  59.0 |
# | FRA_ANDROID_FEMALE_24_30 |  59.0 |
# | USA_IOS_MALE_31_40       |  54.0 |
# | DEU_ANDROID_FEMALE_31_40 |  49.0 |
# +--------------------------+-------+

# Dikkat! List comprehension ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18. Bunları groupby'a alıp price ortalamalarını almak gerekmektedir

# Başlayalım =D

agg_df["customers_level_based"] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'AGE_CAT']].agg('_'.join, axis=1).str.upper()
print(agg_df)
print("***********************************")

# Gruplayip ortalamasini atayalim
agg_df = agg_df.groupby(["customers_level_based"]).agg({"PRICE": "mean"})
agg_df = agg_df.reset_index()
print(agg_df)
print("***********************************")



######################################
# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız
######################################

# • Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# • Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# • Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

# Segment columunu olusturuyoruz.
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
print(agg_df)
print("***********************************")

# Segmentleri betimleyelim (ortalama, max ve toplam)
print(agg_df.groupby(["SEGMENT"]).agg({"PRICE": ["mean","max","sum"]}))
print("***********************************")



######################################
# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz
######################################

# • 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
tahmin01 = "TUR_ANDROID_FEMALE_31_40"

print(tahmin01 + " için tahmini gelir: " + str(agg_df[agg_df["customers_level_based"] == tahmin01]["PRICE"].values))
print("***********************************")


# • 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
tahmin02 = "FRA_IOS_FEMALE_31_40"

print(tahmin02 + " için tahmini gelir: " + str(agg_df[agg_df["customers_level_based"] == tahmin02]["PRICE"].values))
print("***********************************")













 





