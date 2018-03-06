import pandas as pd
df = pd.DataFrame\
    ({\
        'ID': ['red', 'yellow', 'blue'],
        'Col a': [0.5, 0.25, 0.125],
        'Col b': [0.6, 0.26, 0.126]\
    })

print(df)

my_dict = df.to_dict('list')
print(my_dict)

my_dict = df.set_index('ID').T.to_dict('list')
print(my_dict)
