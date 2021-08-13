from numpy import average
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["average"]], ["data plotting"], show_hist= False)
fig.show()

dataset = []
data = df["average"].tolist()
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
stdev = statistics.stdev(dataset) 

print(mean, stdev)