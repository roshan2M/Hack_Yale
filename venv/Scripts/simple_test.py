import pandas as pd

def assetTest(set):
    "make sure long term and short term assets add to total assets"
    ids = []
    for i in range(len(set.assets)):
        if not((set.iat[i,9] + set.iat[i,10]) > set.iat[i,3]-0.01 and (set.iat[i,9]+set.iat[i,10])<set.iat[i,3]+0.01):
            ids.append(set.iat[i,1])

    return(ids)
