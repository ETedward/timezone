import os
import pandas as pd

CSV_Path = os.path.join('timePeople.csv')
df = pd.read_csv(CSV_Path, index_col=0, usecols=[0,1,2,3,4])

#cl1 = df["Time"].tolist()
cl2 = df["People"].tolist()
cl3 = df["Cities"].tolist()

import plotly.graph_objs as go
import plotly.offline as offline

print(cl2)
print(cl3)

cl1 = ['-11','-10','-8','-7','-6','-5','-4','-3','-2','-1','0','1','2','3','4','5','6','7','8','9','10','11']

trace1 = go.Bar(
    x=cl1,
    y=cl2,
    name='Students'
)

trace2 = go.Bar(
    x=cl1,
    y=cl3,
    name='Cities'
)

layout = go.Layout(
    title="Princeton by the Timezone",
    xaxis_title="UTC Timezone",

    #barmode='group'
)

data = [trace1, trace2]

fig = go.Figure(
    data = data,
    layout = layout,
)

fig.layout.update(
    xaxis_type='category'
)

offline.plot(fig, filename='group-bar.html')