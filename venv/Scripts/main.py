import csv
import os
import distribution
import outliers
import simple_test
import pandas as pd
import numpy as np

def pandaStrtoFlt(temp):
    "converts the applicable string fields to integers"
    temp.assets = temp.assets.astype(float)
    temp.profits = temp.profits.astype(float)
    temp.pd = temp.pd.astype(float)
    temp.liabilities = temp.liabilities.astype(float)
    temp.assets_short_term = temp.assets_short_term.astype(float)
    temp.assets_long_term = temp.assets_long_term.astype(float)
    temp.equity = temp.equity.astype(float)
    temp.sales = temp.sales.astype(float)
    temp.employees = temp.employees.astype(int)
    return temp

my_path = os.path.abspath(os.path.dirname(__file__))
parent_directory1 = os.path.split(my_path)[0]
parent_directory2 = os.path.split(parent_directory1)[0]
path1 = os.path.join(parent_directory2, 'Data', 'report1.csv')
path2 = os.path.join(parent_directory2, 'Data', 'report2.csv')
path3 = os.path.join(parent_directory2, 'Data', 'report3.csv')
path4 = os.path.join(parent_directory2, 'Data', 'report4.csv')

Y1 = pd.read_csv(path1)
Y2 = pd.read_csv(path2)
Y3 = pd.read_csv(path3)
Y4 = pd.read_csv(path4)

Y1 = pandaStrtoFlt(Y1)
Y2 = pandaStrtoFlt(Y2)
Y3 = pandaStrtoFlt(Y3)
Y4 = pandaStrtoFlt(Y4)

trainingFrames = [Y1, Y2]
YT = pd.concat(trainingFrames)

print(simple_test.assetTest(Y4)) #tests if assets add up - returns a list of all ids who do not match

"""
print(outliers.determineOutliers(Y3,3))
print(outliers.determineOutliers(Y4,3))"""
"""
hist1 = distribution.stdInterval(Y1,4)
hist2 = distribution.stdInterval(Y2,4)
hist3 = distribution.stdInterval(Y3,4)
hist4 = distribution.stdInterval(Y4,4)

print("fhidf")
print(hist1)

ans1 = distribution.findAnomalies(hist1,hist2,hist3,0.1)
ans2 = distribution.findAnomalies(hist1,hist2,hist4,0.1)

print(ans1)
print(ans2)
"""
