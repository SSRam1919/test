import pandas as pd

lis = {'name': ['ram','sri','sai'], 'marks':[38,67,98]}
f = ['a','b','c']
df = pd.DataFrame(lis, index = f)

print(df)