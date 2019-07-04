import pandas as pd

# df = pd.read_csv('C:\python\SBERP_990601_190620.csv')
# print(df[df.loc[:, ['<LOW>','<HIGH>']] >= 200].isnull().sum())

df = pd.read_csv(r'C:\Users\OLEGWORKPC\Desktop\Parse\ListOfHH.ru.csv')
print(df.loc[1])