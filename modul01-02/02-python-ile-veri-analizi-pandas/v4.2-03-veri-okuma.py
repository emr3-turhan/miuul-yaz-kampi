################################################################################
# Veri Okuma (Reading Data)
################################################################################
import pandas as pd

# CSV dosyasını okuyalım.
df = pd.read_csv("modul01-02/02-python-ile-veri-analizi-pandas/advertising.csv")

# İlk 5 satırı gözlemleyelim.
print(df.head())

# pandas cheatsheet