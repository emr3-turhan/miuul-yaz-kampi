##############################################################################################
# Matplotlib Özellikleri
##############################################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Eğer veri setindeki tüm columnları göremiyorsanız.
# pd.set_option("display.max_columns", None)
# çalıştırabilirsiniz.

########################
# plot
########################

x = np.array([1,8])

y = np.array([0,150])

plt.plot(x,y)
plt.show()

# Nokta grafik çizmek için.
plt.plot(x,y,'o')
plt.show()

# Daha fazla nokta

x = np.array([1,8,10,12,14,16,18,20,22,24,26,28,30])
y = np.array([1,150,200,250,300,350,400,450,500,550,600,650,700])

plt.plot(x,y,'o')
plt.show()


########################
# marker
########################

y = np.array([13,28,11,100])
plt.plot(y, marker='o')
plt.show()

plt.plot(y, marker='*')
plt.show()

markers = ['o','*','.','x','X','+','P','s','D','d','p','H','h','^']

########################
# line
########################

y = np.array([13,28,11,100])
plt.plot(y)
plt.show()

plt.plot(y, linestyle='dotted')
plt.show()

linestyle = ['solid','dashed','dashdot','dotted']

color = ["r","g","b","c","m","y","k","w"]

########################
# mutiple lines
########################

x = np.array([23,18,31,10])
y = np.array([13,28,11,100])

plt.plot(x)
plt.plot(y)
plt.show()

########################
# labels
########################

x = np.array([23,18,31,10])
y = np.array([13,28,11,100])
plt.plot(x,y)
# Başlık
plt.title("Ana Başlık")
plt.show()

# x ekseni başlık
plt.xlabel("x ekseni başlık")


# y ekseni başlık
plt.ylabel("y ekseni başlık")
plt.show()

# 
plt.grid()
plt.show()


########################
# subplots
########################

# 1. subplot
x = np.array([23,18,31,10])
y = np.array([13,28,11,100])
plt.subplot(1,2,1)
plt.title("1. subplot")
plt.plot(x,y)

# 2. subplot
x = np.array([123,182,312,120])
y = np.array([133,218,111,100])
plt.subplot(1,2,2)
plt.title("2. subplot")
plt.plot(x,y)

plt.show()








