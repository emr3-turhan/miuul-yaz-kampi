################################################################################
# Koşullu Seçim (Conditional Selection)
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

# Dataframe'lerin indexlerine kosullu ifade sorguları yapılabilir.
print(df[df["age"] > 50].head())
print(df[df["age"] > 50]["age"].count())

# Direk değikeni istersek eğer loc kullanmalıyız.
print(df.loc[df["age"] > 50, ["age","class"]].head())

# Birden fazla koşullu ifade kullanacaksak koşullar " (kosul) & (kosul) " şeklinde yazılmalıdır.
print(df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age","class"]].head())

# Daha fazla kosul istersek ekleme yapabiliriz.
print(df.loc[(df["age"] > 50)
           & (df["sex"] == "male")
           & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton"))
           , ["age","class","embark_town"]].head())


# Bu dataframe'i yeni dataframe yapalım.
df_new = df.loc[(df["age"] > 50)
           & (df["sex"] == "male")
           & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton"))
           , ["age","class","embark_town"]]

# Dataframe'deki embark_town değişkeninin sayılarına bakalım.
print(df_new["embark_town"].value_counts())