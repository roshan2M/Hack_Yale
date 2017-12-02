import csv
import os
import AnomalyDetection


assets = []
profits = []
liabilities = []
assets_st = []
assets_lt = []
equity = []
sales = []
employees = []

my_path = os.path.abspath(os.path.dirname(__file__))
parent_directory1 = os.path.split(my_path)[0]
parent_directory2 = os.path.split(parent_directory1)[0]
path = os.path.join(parent_directory2, 'Data', 'report1.csv')

with open(path) as f:
    rows = csv.reader(f)
    for row in rows:
        assets.append(row[3])
        profits.append(row[4])
        liabilities.append(row[8])
        assets_st.append(row[9])
        assets_lt.append(row[10])
        equity.append(row[11])
        sales.append(row[12])
        employees.append(row[13])

assets = assets[1:]
profits = profits[1:]
liabilities = liabilities[1:]
assets_st = assets_st[1:]
assets_lt = assets_lt[1:]
equity = equity[1:]
sales = sales[1:]
employees = employees[1:]

AnomalyDetection.plotData(assets)
