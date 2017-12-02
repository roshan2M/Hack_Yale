import csv
import os
import AnomalyDetection
import pandas as pd
import numpy as np

my_path = os.path.abspath(os.path.dirname(__file__))
parent_directory1 = os.path.split(my_path)[0]
parent_directory2 = os.path.split(parent_directory1)[0]
path1 = os.path.join(parent_directory2, 'Data', 'report1.csv')
path2 = os.path.join(parent_directory2, 'Data', 'report2.csv')
path3 = os.path.join(parent_directory2, 'Data', 'report3.csv')
path4 = os.path.join(parent_directory2, 'Data', 'report4.csv')

Y1 = pd.read_csv(path1)#,dtype = np.float64)
Y2 = pd.read_csv(path2)
Y3 = pd.read_csv(path3)
Y4 = pd.read_csv(path4)

frames = [Y1,Y2,Y3,Y4]
YT = pd.concat(frames)

#print(assets)
X = []
for i in range(len(YT)):
    X.append(i)


Xp = pd.DataFrame(X,columns = ['Index'])
#Yp = pd.DataFrame(assets,columns = ['Assets'])
YT.assets = YT.assets.astype(float)
YT.profits = YT.profits.astype(float)
YT.pd = YT.pd.astype(float)
YT.liabilities = YT.liabilities.astype(float)
YT.assets_short_term = YT.assets_short_term.astype(float)
YT.assets_long_term = YT.assets_long_term.astype(float)
YT.equity = YT.equity.astype(float)
YT.sales = YT.sales.astype(float)
YT.employees = YT.employees.astype(int)

print(YT.assets)
print(YT.profits)

print(YT.assets)

#print(Xp)
#print(Yp)
#AnomalyDetection.plotData(Yp)

# plot the results

print("Choose Variable to do Anomaly Detection")
print("1. assets")
print("2. profits")
print("3. pd")
print("4. liabilities")
print("5. assets short term")
print("6. assets long term")
print("7. equity")
print("8. sales")
print("9. employees")

choice = input("Choice?")

if choice == 1:
    AnomalyDetection.plot_results(Xp, YT.assets, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Assets")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.assets, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 1:
    AnomalyDetection.plot_results(Xp, YT.assets, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Assets")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.assets, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 1:
    AnomalyDetection.plot_results(Xp, YT.assets, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Assets")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.assets, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 1:
    AnomalyDetection.plot_results(Xp, YT.assets, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Assets")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.assets, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 2:
    AnomalyDetection.plot_results(Xp, YT.profits, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Profits")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.profits, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 3:
    AnomalyDetection.plot_results(Xp, YT.pd, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Pd")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.pd, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 4:
    AnomalyDetection.plot_results(Xp, YT.liabilities, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Liabilities")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.liabilities, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 5:
    AnomalyDetection.plot_results(Xp, YT.assets_short_term, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Short Term Assets")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.assets_short_term, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 6:
    AnomalyDetection.plot_results(Xp, YT.assets, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Assets")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.assets, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))

if choice == 1:
    AnomalyDetection.plot_results(Xp, YT.assets, window_size=100, text_xlabel="Index", sigma_value=3,
                 text_ylabel="Assets")
    events = AnomalyDetection.anomalies_stationary_stddev(YT.assets, window_size=5, sigma=3)

    # Display the anomaly dict
    print("Information about the anomalies model:{}".format(events))
