import matplotlib.pyplot as plt
import pandas as pd
from numpy import array


df = pd.read_csv('/Users/shanehower/Desktop/genre_code_vg.csv')
df['Critic_Score'] = df['Critic_Score'].astype('float64')
df['Critic_Count'] = df['Critic_Count'].astype('float64')
df['User_Count'] = df['User_Count'].astype('float64')


#changing the list to a numpy array which can be used for color in matplotlib
arr_genre = array(list(df['Genre_Code']))

def plot_scatter(col1, col2):
    #first had to use SQL and add a column that was a number code for the genre.
    #then had to make a list of that column and convert it into a numpy array
    #which for some reason is a valid argument for color in matplotlib

    plt.scatter(df[col1], df[col2], c = arr_genre)
    if col1 == 'Year'  or col2 == 'Year':
        #eliminate 0 entries for readability when Year is involved  
        plt.xlim((1975,2020))
    plt.colorbar(ticks=range(13))
    plt.title("{0} vs. {1}".format(col1, col2))
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()

plot_scatter('Year', 'Global_Sales')
