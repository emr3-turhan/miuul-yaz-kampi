###############################################################################
# Fancy indexing
###############################################################################
import numpy as np

# Numpy array tanımlaması
v = np.arange(0,30,3)

print(v[1])
print(v[4])

# Index değerlerini tutacak liste
catch = [1,2,3]

# Fancy index sayesinde listelerden index değerleri alınabilir.
print(v[catch])


