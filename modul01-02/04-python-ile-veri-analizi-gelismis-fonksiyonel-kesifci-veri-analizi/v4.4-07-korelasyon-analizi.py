########################################################################################################################
# Korelasyon Analizi (Analysis of Correlations)
########################################################################################################################

import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Eğer veri setindeki tüm columnları göremiyorsanız.
pd.set_option("display.max_columns", None)
# çalıştırabilirsiniz.

df= pd.read_csv("modul01-02/04-python-ile-veri-analizi-gelismis-fonksiyonel-kesifci-veri-analizi/breast_cancer.csv")
df = df.iloc[:,1:-1]
#print(df.head())

num_cols = [col for col in df.columns if df[col].dtype in ["int64","float64"]]

corr = df[num_cols].corr()
#print(corr)

sns.set(rc={'figure.figsize':(12,12)})
sns.heatmap(corr,cmap="RdBu")
#plt.show()



##############################
# Yüksek korelasyonlu değişkenlerin silinmesi
##############################

cor_matrix  = df.corr().abs() # abs() mutlak değerleri alır.

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
#print(upper_triangle_matrix)

drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
#print(drop_list)

#print(cor_matrix[drop_list])

#print(df.drop(drop_list,axis=1))

def high_correlated_cols(dataframe,plot=False,corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize':(15,15)})
        sns.heatmap(cor_matrix,cmap="RdBu")
        plt.show()
    return drop_list

print(high_correlated_cols(df))
drop_list = high_correlated_cols(df,plot=True)
drop_list = high_correlated_cols(df.drop(drop_list,axis=1),plot=True)





