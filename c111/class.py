import pandas as pd
import csv 
import plotly.figure_factory as ff
import statistics
import random

data = pd.read_csv("studentMarks.csv")
mark_list = data["Math_score"].tolist()

graph = ff.create_distplot([mark_list],["math scores"], show_hist = False)
#graph.show()

popmean = statistics.mean(mark_list)
popsd = statistics.stdev(mark_list)

#print(popmean)
#print(popsd)
def randomsamples(counter): #counter = 100
    sampledata = []
    for i in range (0,counter):
        randomsample = random.randint(0,len(mark_list-1))
        value = mark_list[randomsample]
        sampledata.append(value)
    samplemean = statistics.mean(sampledata)
    return samplemean

#to find the mean of the samples for 1k times
samplelist = []
for i in range (0,1000):
    meanset = randomsamples(100)
    samplelist.append(meanset)
smean = statistics.mean(samplelist)
ssd = statistics.stdev(samplelist)
print(smean, ssd)

#to cakculate the z score
zscore = (smean - popmean)/ssd
