# def plot_series(time, series, format="-", start=0, end=None, label=None):
#    plt.plot(time[start:end], series[start:end], format, label=label)
 #   plt.xlabel("Time")
 #   plt.ylabel("Value")
 #   if label:
 #       plt.legend(fontsize=14)
 #   plt.grid(True)


import matplotlib.pyplot as plt
import seaborn as sns

def plot_series(time, series, format = '-', start= 0, end = None, label = None):
    plt.plot(time[start:end], series[start:end], format,label = label)
    plt.xlabel('Time')
    plt.ylabel('Value')

    if label:
        plt.legend(fontsize = 10)

    plt.grid(True)

