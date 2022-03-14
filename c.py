import csv
import plotly.express as c

with open("c.csv")  as f:
    df=csv.DictReader(f)
    fig=c.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()