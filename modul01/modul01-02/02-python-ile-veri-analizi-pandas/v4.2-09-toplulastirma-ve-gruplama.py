############################################################################################
# Toplulaştırma ve Gruplama (Aggregation and Grouping)
############################################################################################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot_table()  (pivot table) haric hepsi group by ile yapılabilir.)

import pandas as pd
import seaborn as sns

# Eğer veri setindeki tüm columnları göremiyorsanız.
# pd.set_option("display.max_columns", None)
# çalıştırabilirsiniz.

# Dataframe oluşturmak için. (titanic veriseti)
df = sns.load_dataset("titanic")

# Dataframe in ilk 5 satırını görmek için.
print(df.head()) 

# Age değerlerinın ortalamasını almak için.
print(df["age"].mean())

# Cinsiyete göre yaş ortalamasını almak için.
print(df.groupby("sex")["age"].mean())

# Agg ile birden fazla metod uygulanabilir.
print(df.groupby(["sex","embark_town"]).agg({"age": ["mean","sum",],"survived":["mean"]}))

# Agg ile birden fazla metod uygulanabilir.
print(df.groupby(["sex","embark_town","class"]).agg({"age": ["mean","sum",],"survived":["mean"],"sex":["count"]}))


