################################################################################
# Apply ve Lambda
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

# Apply satır ve sütunlarda bir fonksiyon çalıştırma imkanı sağlar.
# Lambda kullan at fonksiyon kullanmayı sağlar.

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

# Columnları üzerinde işlem yapıp görüntülemek için tek tek seçmemiz gerekir.
# Bunun önüne geçmek için döngü kullanılabilir.
for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

# Bakalım
print(df.head())

# Bir satıra bir fonksiyonu uygulamak için apply() kullanılır.
df[["age","age2","age3"]].apply(lambda x: x/10).head()

# İçerisinde 'age' isminde bir column varsa onu seçip apply uygulamak için:
print(df.loc[:,df.columns.str.contains("age")].apply(lambda x: x/10).head())

# Daha karışık...
print(df.loc[:,df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head())

# Dışarıdan yazdığımız fonksiyonu da apply() fonksiyonunda kullanabiliriz.

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

print(df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head())

# df.loc[:,["age","age2","age3"]] = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler)

df.loc[:,df.columns.str.contains("age")] = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler)

# Bakalım
print(df.head())




