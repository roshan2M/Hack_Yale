import pandas as pd

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

def determineOutliers(set,dev):
    "determines outliers by 3 std's away from the mean"
    mean = computeMean(set)
    std = computeStd(set)
    cnt_assets = 0
    cnt_profits = 0
    cnt_liabilities = 0
    cnt_assets_short = 0
    cnt_assets_long = 0
    cnt_equity = 0
    cnt_sales = 0
    for i in range(len(set.assets)):
        if not(set.iat[i,3] > mean[0]-dev*std[0] and set.iat[i,3] < mean[0]+dev*std[0]):
            cnt_assets+=1
        if not(set.iat[i,4] > mean[1]-dev*std[1] and set.iat[i,4] < mean[1]+dev*std[1]):
            cnt_profits+=1
        if not(set.iat[i,8] > mean[2]-dev*std[2] and set.iat[i,8] < mean[2]+dev*std[2]):
            cnt_liabilities+=1
        if not(set.iat[i,9] > mean[3]-dev*std[3] and set.iat[i,9] < mean[3]+dev*std[3]):
            cnt_assets_short+=1
        if not(set.iat[i,10] > mean[4]-dev*std[4] and set.iat[i,10] < mean[4]+dev*std[4]):
            cnt_assets_long+=1
        if not(set.iat[i,11] > mean[5]-dev*std[5] and set.iat[i,11] < mean[5]+dev*std[5]):
            cnt_equity+=1
        if not(set.iat[i,12] > mean[6]-dev*std[6] and set.iat[i,12] < mean[6]+dev*std[6]):
            cnt_sales+=1

    outliers = [cnt_assets,cnt_profits,cnt_liabilities,cnt_assets_short,cnt_assets_long,cnt_equity,cnt_sales]
    return(outliers)
