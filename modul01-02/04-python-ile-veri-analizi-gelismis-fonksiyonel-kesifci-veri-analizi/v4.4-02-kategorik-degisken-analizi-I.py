############################################################################################
# Kategorik Değişken Analizi I: (Analysis of Categorical Variables)
############################################################################################
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


print(df["embarked"].value_counts())
print(df["sex"].unique())
print(df["sex"].nunique())

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]
print(cat_cols)

# survived kategorik degiskendir ama yukaridaki yontemle yakalayamdik

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]]
print(num_but_cat)

# Çok fazla kategorik sınıfı olan değişkenler ayırt ediciliğini yitirirler onların tespitini yapalım.
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]]
print(cat_but_car)
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

print(df[cat_cols].nunique())


def cat_summary(dataframe,col_name):
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##############################################################")

cat_summary(df,"sex")

for col in cat_cols:
    cat_summary(df,col)

def cat_summary(dataframe,col_name,plot=False):
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##############################################################")

    if plot:
        sns.countplot(x=dataframe[col_name],data=dataframe)
        plt.show(block=True)

cat_summary(df,"sex",plot=True)

# for col in cat_cols:
#     if df[col].dtype == "bool":

#         print("Bool tespit edildi")
#         cat_summary(df,col,plot=False)
        
#     else:
#         cat_summary(df,col,plot=True)

for col in cat_cols:
    if df[col].dtype == "bool":
        df[col] = df[col].astype("int64")
        cat_summary(df,col,plot=True)
        
    else:
        cat_summary(df,col,plot=True)
        





