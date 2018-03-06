import pandas as pd

df1 = pd.read_excel("dummy data for pd df.xlsx")

print(df1)

my_dict = dict([(i, [a, b, c]) for i, a, b, c in zip(df1.ID, df1.A, df1.B, df1.C)])
print(my_dict)

my_dict = df1.to_dict('list')
print(my_dict)

my_dict = df1.set_index('ID').T.to_dict('list')
print(my_dict)
