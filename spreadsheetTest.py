import pandas as pd

df = pd.read_excel('test.xlsx')


test = df.iloc[1,2]
print(test)