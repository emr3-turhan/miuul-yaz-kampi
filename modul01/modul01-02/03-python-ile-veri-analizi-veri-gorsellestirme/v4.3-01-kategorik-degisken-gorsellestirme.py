##############################################################################################
# VERİ GÖRSELLESTİRME: MATPLOTLIB & SEABORN
##############################################################################################

##############################################################################################
# MATPLOTLIB
##############################################################################################

# Kategorik Değişken: sütun grafik, countplot bar
# Sayısal Değişken: hist, boxplot

# Veri görselleştirmenin asıl yapılması gereken yer BM (iş zekası) araçlarıdır. Veriye dahayakındır.
# Raporlama için farklı bir ortam kullanılmalıdır.

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

# Matplotlib ile sütun grafikleri çizmek için.
df["sex"].value_counts().plot(kind="bar")

# Grafiği göstermek için
plt.show()