import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def computeMean(set):
    "inputs a panda DataFrame of any length (14 columns) and outputs a numpy array with 7 outputs"
    # Assets, Profits, Liabilities, Short term assets, Long term assets, equity, and sales

    mean = []
    mean.append(set.assets.mean())
    mean.append(set.profits.mean())
    mean.append(set.liabilities.mean())
    mean.append(set.assets_short_term.mean())
    mean.append(set.assets_long_term.mean())
    mean.append(set.equity.mean())
    mean.append(set.sales.mean())

    return mean

def computeStd(set):
    "same parameters and return as computeMean but std dev instead of mean"
    std = []
    std.append(set.assets.std())
    std.append(set.profits.std())
    std.append(set.liabilities.std())
    std.append(set.assets_short_term.std())
    std.append(set.assets_long_term.std())
    std.append(set.equity.std())
    std.append(set.sales.std())

    return std

def computeMin(set):
    "same parameters and return as computeMean but min dev instead of mean"
    min = []
    min.append(set.assets.min())
    min.append(set.profits.min())
    min.append(set.liabilities.min())
    min.append(set.assets_short_term.min())
    min.append(set.assets_long_term.min())
    min.append(set.equity.min())
    min.append(set.sales.min())

    return min

def computeMax(set):
    "same parameters and return as computeMean but max dev instead of mean"
    max = []
    max.append(set.assets.max())
    max.append(set.profits.max())
    max.append(set.liabilities.max())
    max.append(set.assets_short_term.max())
    max.append(set.assets_long_term.max())
    max.append(set.equity.max())
    max.append(set.sales.max())

    return max

def stdInterval(set,interval):
    "accepts a panda dataframe, the amout of intervals the data will be split into and the specific category"
    #returns a 2d numpy array where each row is a different data set ie. assets, profits etc.
    #each column is a different interval

    """sorted_assets = set.assets.sort_values()
    sorted_profits = set.profits.sort_values()
    sorted_liabilities = set.liabilities.sort_values()
    sorted_assets_short_term = set.assets_short_term.sort_values()
    sorted_assets_long_term = set.assets_long_term.sort_values()
    sorted_equity = set.equity.sort_values()
    sorted_sales = set.sales.sort_values()"""

    min = computeMin(set)
    max = computeMax(set)

    scaled = set.copy()

    #scaling all values from 0-100
    for i in range(len(set.assets)):
        scaled.iat[i,3] = set.iat[i,3]*100/max[0]
        scaled.iat[i,4] = set.iat[i,4]*100/max[1]
        scaled.iat[i,8] = set.iat[i,8]*100/max[2]
        scaled.iat[i,9] = set.iat[i,9]*100/max[3]
        scaled.iat[i,10] = set.iat[i,10]*100/max[4]
        scaled.iat[i,11] = set.iat[i,11]*100/max[5]
        scaled.iat[i,12] = set.iat[i,12]*100/max[6]

    #1st interval
    interWidth =(100/interval)
    hist = np.zeros((7,interval),dtype=np.int)

#filling the histogram with values - scans through all 50 000 values and its sub sections
    for j in range(len(set.assets)):
        for i in range(1,interval+1):
            if(scaled.iat[j,3] <i*interWidth and scaled.iat[j,3] > (i-1)*interWidth):
                hist[0,i-1] += 1
            if(scaled.iat[j,4] <i*interWidth and scaled.iat[j,4] > (i-1)*interWidth):
                hist[1,i-1] += 1
            if(scaled.iat[j,8] < i*interWidth and scaled.iat[j,8] > (i-1)*interWidth):
                hist[2,i-1] += 1
            if(scaled.iat[j,9] < i*interWidth and scaled.iat[j,9] > (i-1)*interWidth):
                hist[3,i-1] += 1
            if(scaled.iat[j,10] < i*interWidth and scaled.iat[j,10] > (i-1)*interWidth):
                hist[4,i-1] += 1
            if(scaled.iat[j,11] < i*interWidth and scaled.iat[j,11] > (i-1)*interWidth):
                hist[5,i-1] += 1
            if(scaled.iat[j,12] < i*interWidth and scaled.iat[j,12] > (i-1)*interWidth):
                hist[6,i-1] += 1


    scaled.drop('rating',axis = 1,inplace = True)
    scaled.drop('id',axis = 1,inplace = True)
    scaled.drop('reporting_date',axis = 1,inplace = True)
    scaled.drop('pd',axis = 1,inplace = True)
    scaled.drop('maturity_date',axis = 1,inplace = True)
    scaled.drop('state',axis = 1,inplace = True)
    scaled.drop('employees',axis = 1,inplace = True)

    #print(scaled)
    print("hdf")
    #plt.figure();
    #scaled.plot.hist(bins = 20)
    #plt.show()
    return (hist)


    #frames = [sorted_assets, sorted_profits, sorted_liabilities, sorted_assets_short_term,sorted_assets_long_term,sorted_equity,sorted_sales]
    #sorted_total = pd.concat(frames,axis = 1)

    #print(sorted_total)

def fillAnsArr(set1,set2,alpha,set,setType):
    "fills output matrix with correct and incorrect data in dictionaries all in a 2d array"
    #setType is an int determining what type of set we are analyzing
    #returns a 1d array of dictionaries (2)
    correct = {}
    incorrect = {}
    print(set)
    for i in range(len(set[0])): # how many intervals
        avg = (set1[0][i] + set2[0][i])/2
        if(set[setType][i] > avg*(1-alpha) and set[setType][i]<avg*(1+alpha)):
            correct[i] = set[setType][i]
        else:
            incorrect[i] = set[setType][i]
    return [correct,incorrect]

def findAnomalies (set1,set2,seta,alpha):
    "finds anomalies in a set using tolerance alpha(alpha must be from 0-1)"
    #set1 2 3 are 2d numpy arrays with 7 rows and the same number of columns (each column is a interval)

    answer = []
    for i in range(0,7): #going hrough the different columns
        answer.append(fillAnsArr(set1,set2,alpha,seta,i))

    return answer
