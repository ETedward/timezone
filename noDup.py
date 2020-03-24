import os
import pandas as pd

CSV_Path = os.path.join('tigerbook_time.csv')
df = pd.read_csv(CSV_Path, index_col=0, usecols=[0,1,2])

mydf = df.groupby(['Hometown']).size().reset_index()
mydf.rename(columns = {0: 'frequency'}, inplace = True)
mydf.to_csv('tigerFreq.csv')

""" 
column_names = ["ID", "Location", "Frequency"]
df2 = pd.DataFrame(columns = column_names)

i = 0;

for region, df_region in df.groupby('Hometown'):
    print(df_region)
    #print("frequencey is", (df_region.size / 2))
    df.loc[i] = ['name' + str(i)] + list(2)
    i = i + 1

print(df2)
"""