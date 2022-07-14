##############################################################################################
# Seaborn ile veri görselleştirme
##############################################################################################
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x=df["sex"],data=df)
plt.show()

df["sex"].value_counts().plot(kind="bar")
plt.show()

#########################
# Sayısal Değişken Görselleştirme
#########################

sns.boxplot(x=df["total_bill"])
plt.show()