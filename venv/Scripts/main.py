import csv
import os
import AnomalyDetection
import pandas as pd


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

X = []
Y = []
for i in range(len(assets)):
    X.append(i)


Xp = pd.DataFrame(X,columns = ['Index'])
Yp = pd.DataFrame(assets,columns = ['Assets'])
Yp.Assets = Yp.Assets.astype(float)

#print(Xp)
#print(Yp)

# plot the results
AnomalyDetection.plot_results(Xp, Yp, window_size=10, text_xlabel="Index", sigma_value=3,
             text_ylabel="Assets")
events = AnomalyDetection.anomalies_stationary_stddev(Yp, window_size=5, sigma=3)

# Display the anomaly dict
print("Information about the anomalies model:{}".format(events))
