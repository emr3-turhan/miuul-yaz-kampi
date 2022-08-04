################################################################################
# Loc ve Iloc
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

# iloc: integer based selection
df.iloc[0:3]

print(df.iloc[0:3])

print(df.iloc[0,0])

# loc: label based selection
df.loc[0:3]

print(df.loc[0:3])

# iloc bizim bildiğimiz index mantığı ile veri setimizi seçerken loc bizim bildiğimiz label mantığı ile veri setimizi seçer.
# Yani değer ile seçme işlemi yapmak istersek loc kullanırız.
# Örneğin:

df.loc[0:3, "age"]
# Çalışırken df.iloc[0:3, "age"] çalışmaz. (integer değil)

# Yine fancy indexing kullanmak istersek loc kullanırız.
# Örneğin:
col_names = ["age","embarked","alive"]

