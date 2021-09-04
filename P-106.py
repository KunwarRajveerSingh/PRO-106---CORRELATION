import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x": marks_in_percentage, "y": days_present}

def findCorrelation(datasources):
    correlation = np.corrcoef(datasources["x"], datasources["y"])
    print("Correlation betweewn Marks and Days:- \n--->",correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"

    datasources = getDataSource(data_path)
    findCorrelation(datasources)
    plotFigure(data_path)

setup()
