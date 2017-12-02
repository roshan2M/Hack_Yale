import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections
from itertools import count

def plotData(val):
    plt.plot(val)
    plt.show()

def plot_simple(val):
    data = pd.DataFrame(val,columns=['assets'])
    print(data.head())

def computeMovingAvg(val,window_size):
    "computes the moving average using convolution of two sequenes"
    #takes dataset(in pandas DataFrame format) and the window size
    #returns ndarray of linear convolution

    window = np.ones(int(window_size))/float(window_size)
    vallist = list(val.values.flatten())
    valnp = np.array(vallist)
    #valnpf = np.float32(valnp)

    return np.convolve(valnp,window,'same')

def anomalies_stationary_stddev(y,window_size,sigma = 1.0):
    "returns all anomalies and its stationary standard deviation"
    #takes in a data set (pandas DataFrame format)
    #takes in window_size
    #sigma is the value for standard deviation

    #returns an int (standard deviation)
    #returns a dictionary with all anomalies

    avg = computeMovingAvg(y,window_size)
    avg_list = avg.tolist()
    yt = list(y.values.flatten())

    #print("hello")
    #print(avg)
    #print(avg_list)
    #print(yt)

    residual = yt - avg


    #calculate variation
    std = np.std(residual)
    return {'standard_deviation': round(std, 3),
            'anomalies_dict': collections.OrderedDict([(index, y_i) for
                                                       index, y_i, avg_i in zip(count(), yt, avg)
              if (y_i > avg_i + (sigma*std)) | (y_i < avg_i - (sigma*std))])}

def anomalies_rolling_stddev(y,window_size,sigma = 1.0):
    "returns all anomalies and its rolling standard deviation"
    #same as stationary but rolling std dev instead of anomalies_stationary_stddev

    avg = computeMovingAvg(y,window_size)
    avg_list = avg.tolist()
    residual = y-avg

    #calculate variation via std dev
    testing_std = pd.rolling_std(residual, window_size)
    testing_std_as_df = pd.DataFrame(testing_std)
    rolling_std = testing_std_as_df.replace(np.nan,
                                  testing_std_as_df.ix[window_size - 1]).round(3).iloc[:,0].tolist()
    std = np.std(residual)
    return {'stationary standard_deviation': round(std, 3),
            'anomalies_dict': collections.OrderedDict([(index, y_i)
                                                       for index, y_i, avg_i, rs_i in izip(count(),
                                                                                           y, avg_list, rolling_std)
              if (y_i > avg_i + (sigma * rs_i)) | (y_i < avg_i - (sigma * rs_i))])}

# This function is repsonsible for displaying how the function performs on the given dataset.
def plot_results(x, y, window_size, sigma_value=1,
                 text_xlabel="X Axis", text_ylabel="Y Axis", applying_rolling_std=False):
    """ Helps in generating the plot and flagging the anamolies.
        Supports both moving and stationary standard deviation. Use the 'applying_rolling_std' to switch
        between the two.
    Args:
    -----
        x (pandas.Series): dependent variable
        y (pandas.Series): independent variable
        window_size (int): rolling window size
        sigma_value (int): value for standard deviation
        text_xlabel (str): label for annotating the X Axis
        text_ylabel (str): label for annotatin the Y Axis
        applying_rolling_std (boolean): True/False for using rolling vs stationary standard deviation
    """
    plt.figure(figsize=(15, 8))
    plt.plot(x, y, "k.")
    print("plot")
    print(y)
    y_av = computeMovingAvg(y, window_size)
    plt.plot(x, y_av, color='green')
    plt.xlim(0, 50001)
    plt.xlabel(text_xlabel)
    plt.ylabel(text_ylabel)

    # Query for the anomalies and plot the same
    events = {}
    if applying_rolling_std:
        events = anomalies_rolling_stddev(y, window_size=window_size, sigma=sigma_value)
    else:
        events = anomalies_stationary_stddev(y, window_size=window_size, sigma=sigma_value)

    print("hello")
    print (events['anomalies_dict'].keys())
    print (events['anomalies_dict'].values())
    x_anomaly = np.fromiter(events['anomalies_dict'].keys(), dtype=int, count=len(events['anomalies_dict']))
    y_anomaly = np.fromiter(events['anomalies_dict'].values(), dtype=float,
                                            count=len(events['anomalies_dict']))
    plt.plot(x_anomaly, y_anomaly, "r*", markersize=12)

    # add grid and lines and enable the plot
    plt.grid(True)
    plt.show()
