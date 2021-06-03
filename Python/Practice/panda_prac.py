import numpy as np
import pandas as pd

labels = ['A', 'B', 'C', 'D']
ar = np.array([100, 200, 300, 400])

series = pd.Series(data=ar, index=labels)

#print(series)

d = {"X":0,"Y":1,"Z":2}
ser = pd.Series(d)
#print(ser)

ser2 = pd.Series([80, 90, 85], ["Michael", "John", "Arthur"])
#print (ser2)
#print(ser+ser2)
#print(ser.add(ser2,fill_value=0))
#print(ser2.keys())
df = pd.read_csv('cancer.csv')
print(df.head())