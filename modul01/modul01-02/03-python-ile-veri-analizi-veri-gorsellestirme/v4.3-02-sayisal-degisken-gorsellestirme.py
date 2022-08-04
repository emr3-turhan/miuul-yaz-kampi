##############################################################################################
# Sayısal Değişkenlerin Görselleştirilmesi
##############################################################################################

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

# Histogram grafiği çizmek için.
plt.hist(df["age"])
plt.show()

# Kutu grafiği çizmek için. Kutu grafikleri ile aynı zamanda aykırı değerlerin tespiti yapılabilir.
plt.boxplot(df["fare"])
plt.show()

