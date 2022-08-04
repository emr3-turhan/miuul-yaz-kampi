############################################################################################
# Birlestirme (Join) İşlemleri
############################################################################################
import numpy as np
import pandas as pd

m = np.random.randint(1,30,size=(5,3))

df1 = pd.DataFrame(m, columns=["var1","var2","var3"])
df2 = df1 + 99

# Birleştirme işlemi için pd.concat() kullanılır. Indexleri kopyalar. Yani index problemi oluşur
print(pd.concat([df1, df2]))

# Index problemini engellemek için ignore_index=True parametresi kullanılır.
print(pd.concat([df1, df2], ignore_index=True))

########################
# Merge İle Birleştirme İşlemi
########################

df1 = pd.DataFrame({'employees':['john','dennis','mark','maria'],
                    'group':['accounting','engineering','engineering','hr'],})

df2 = pd.DataFrame({'employees':['mark','john','dennis','maria'],
                    'start_date':[2010,2009,2014,2019]})

print(pd.merge(df1, df2))

# on parametresi hangi değişkenleri birleştirmek istiyorsak onu belirtiyoruz.
print(pd.merge(df1, df2, on='employees'))

# Amaç: Her çalışanın müdürünün bilgine erişmek
df3 = pd.merge(df1,df2)

df4 = pd.DataFrame({'group':['accounting','engineering','hr'],
                    'manager':['Caner','Mustafa','Berkcan']})   # müdürler

print(pd.merge(df3, df4))



