import pandas as pd

df=pd.read_csv('students.csv')

def pointCheck(x):
    if x >= 50:
        return("pass")
    else:
        return("fail")

df['situtation']=df['point'].apply(pointCheck)
print(df)
max_Point=df['point'].idxmax()
mın_Point=df['point'].idxmin()
print("The student with the highest marks:",df['name'][max_Point],df['point'].max())
print("The student with the lowest grades:",df['name'][mın_Point],df['point'].min())
print("Students Points:\n",df)
print("avarage Point:",df['point'].mean())