import pandas as pd

df=pd.read_csv('ogrenciler.csv')

def notKontrol(x):
    if x >= 50:
        return("gecti")
    else:
        return("kaldı")

df['gecme durumu']=df['not'].apply(notKontrol)
print(df)
en_yuksek_not_kım=df['not'].idxmax()
en_dusuk_not_kım=df['not'].idxmin()
print("en yuksek not alan ogrenci:",df['isim'][en_yuksek_not_kım],df['not'].max())
print("en dusuk not alan ogrenci:",df['isim'][en_dusuk_not_kım],df['not'].min())
print("ogrenci notlari:\n",df)
print("ortalama:",df['not'].mean())