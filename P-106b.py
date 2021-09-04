import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x": coffee , "y": sleep}

def findCorrelation(datasources):
    correlation = np.corrcoef(datasources["x"], datasources["y"])
    print("Correlation betweewn coffee and sleep:- \n--->",correlation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"

    datasources = getDataSource(data_path)
    findCorrelation(datasources)
    plotFigure(data_path)

setup()