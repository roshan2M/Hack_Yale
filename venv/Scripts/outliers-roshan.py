from scipy import stats
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

Y1 = pd.read_csv(path1)
Y2 = pd.read_csv(path2)
Y3 = pd.read_csv(path3)
Y4 = pd.read_csv(path4)

trainingFrames = [Y1, Y2]
YT = pd.concat(trainingFrames)

assets = np.float64(YT['assets'])
profits = np.float64(YT['profits'])
liabilities = np.float64(YT['liabilities'])
assets_st = np.float64(YT['assets_short_term'])
assets_lt = np.float64(YT['assets_long_term'])
equity = np.float64(YT['equity'])
sales = np.float64(YT['sales'])
employees = np.float64(YT['employees'])

incorrect = []

# Performs the basic tests on the data
def tests(test_set):
    similar_values_check(test_set)

def similar_values_check(set):
    for i in range(len(set)):
        if i != 0:
            if abs(set[3][i] - set[9][i] - set[10][i]) > 0.01:
                incorrect.append(df[i])
            if abs(set[2][i] + set[9][i] - set[8][i] - set[11][i]) > 0.01:
                incorrect.append(set(i))
            if abs(set[8][i] - set[11][i]) < -0.01:
                incorrect.append(set(i))


def out_of_bounds(feature_set, set):
    mean = np.mean(feature_set)
    std = np.std(feature_set)
    for i in range(len(set)):
        if feature_set[i] <= 0 or feature_set[i] < mean - 3 * std or feature_set[i] > mean + 3 * std:
            incorrect.append(set(i))

def out_of_bounds2(df):
    for col in df:
        mean = df[col].mean()
        std = df[col].std()
        for num in col:
            if num < mean - 3 * std or num > mean + 3 * std:
                incorrect.append(df[col])

# Make linear models
def make_linear_models():
    slope1, intercept1, r_value1, p_value1, stderr1 = stats.linregress(assets, profits)
    slope2, intercept2, r_value2, p_value2, stderr2 = stats.linregress(profits, sales)
    # Use to find points outside the line and classify as outliers.
