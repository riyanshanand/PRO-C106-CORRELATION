from statistics import correlation
import plotly.express as px
import csv 
import numpy as np

#Function to generate graph
def plotfigure(datapath):
    with open(datapath) as f:
     df=csv.DictReader(f)
     fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
     fig.show()

#Function to get data
def getdatasource(datapath):
    temp=[]
    icecreamsale=[]
    with open(datapath) as f:
        df = csv.DictReader(f)
        for i in df:
            temp.append(float(i["Marks In Percentage"]))
            icecreamsale.append(float(i["Days Present"]))
    return {"x":temp,"y":icecreamsale}        

#Function to calculate correlation
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

#calling function to create graph
plotfigure("t.csv")
#calling function to get x and y
r=getdatasource("t.csv")
#Calling function to calculate correlation
findcorrelation(r)

