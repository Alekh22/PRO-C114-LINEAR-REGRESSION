import pandas as pd 
import numpy as np
import plotly.express as px
df = pd.read_csv("main4.csv")
print(df.head())
TOEFL= df["TOEFL Score"].tolist()
Chances_of_admit = df["Chance of Admit"].tolist()
TOEFL_array = np.array(TOEFL)
Chance_of_admit = np.array(Chances_of_admit)
m, c = np.polyfit(TOEFL_array,Chance_of_admit,1)
y = []
for x in TOEFL_array:
  y_value = m*x + c
  y.append(y_value)

#plotting the graph
fig = px.scatter(x=TOEFL_array, y=Chance_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line equation',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_array), x1= max(TOEFL_array)
    )
])
fig.show()