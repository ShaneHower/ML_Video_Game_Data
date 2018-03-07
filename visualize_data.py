import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('/Users/shanehower/Desktop/vg_data/publisher_id.csv')
df2 = pd.read_csv('/Users/shanehower/Desktop/vg_data/only_numbered_columns.csv')

def conv_float(x,y):
    x[y] = x[y].astype('float64')
    return x[y]

conv_float(df1,'Critic_Score')
conv_float(df2,'Critic_Score')
conv_float(df1,'Critic_Count')
conv_float(df2, 'Critic_Count')
conv_float(df1, 'User_Count')
conv_float(df2, 'User_Count')
conv_float(df1, 'User_Score')
conv_float(df2, 'User_Score')

feature_label = list(df2.columns.values)

y = np.array(list(df1['Genre_Code']))
X = np.array(list(df2))

def plot_scatter(col1, col2):
    #first had to use SQL and add a column that was a number code for the genre.
    #then had to make a list of that column and convert it into a numpy array
    #which for some reason is a valid argument for color in matplotlib

    plt.scatter(df2[col1], df2[col2], c = y)
    if col1 == 'year'  or col2 == 'year':
        plt.xlim(1975,2020)
    plt.colorbar(ticks=range(13))
    plt.title("{0} vs. {1}".format(col1, col2))
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()

plot_scatter('year', 'publisher_ID')
