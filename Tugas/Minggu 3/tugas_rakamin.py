# -*- coding: utf-8 -*-
"""Tugas Rakamin

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ks4WMVXM7wvZPyUyXGd00W0aPmU42FIf
"""

# Commented out IPython magic to ensure Python compatibility.
# import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

# loading dataset
url = '/content/drive/MyDrive/Dataset AI/Marketing_Campaign_Data_A-21492758-f47a-4913-971e-68c9a721311a.csv'
df = pd.read_csv(url)
df

# Cek tipe data 
df.dtypes

# Menghitung Umur Customer 
from datetime import datetime
from datetime import date
def calculate_age(born):
    born = datetime.strptime(born, "%d-%m-%Y").date()
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

df['age'] = df['DATE_BIRTH'].apply(calculate_age)
df

# Mengategorikan customer sesuai umur
conditions = [
     (df.age < 20),
     (df.age >=20 )&(df.age<30),
     (df.age>=30)&(df.age<40),
     (df.age>=40)&(df.age<50),
     (df.age>=50)&(df.age<60),
     (df.age>=60)
]

values = ['Late_Ten', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Above_Sixty']

df['Kategori_Umur']=np.select(conditions,values)

# Memfilter dataset dengan target = 0, rating = 3 dan appl_datetime antara 1 Januari 2017 sampai 31 Desember 2018
df.APPL_DATETIME = pd.to_datetime(df.APPL_DATETIME)
df2 = df[(df.TARGET ==0)&(df.REGION_RATING_CLIENT_W_CITY==3)&(df.APPL_DATETIME.between('2017-1-1','2018-12-31'))]
df2

# mneghitung jumlah customer per kategori umur
df2['Kategori_Umur'].value_counts()

"""jawaban : 


*   Soal 1 : Above_sixty
*   Soal 2 : Fifty
*   Soal 3 : Thirty


"""