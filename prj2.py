import pandas as pd
import matplotlib.pyplot as plt

# Read in training CSV - already merged values from exoTest.csv 
d = pd.read_csv('./exoTrain.csv')

# print("data:", d.info())
# No null values! :D

#This function plots the flux of 2 random rows over time
def twoRRows():
    # r = d.sample(2)
# Just to ensure I can see one star with an exoplanet & one without
    r2 = d[d['LABEL'] == 2].sample(1)
    r1 = d[d['LABEL'] == 1].sample(1)
    r = pd.concat([r2, r1])

    for index, row in r.iterrows():
        # plt.plot(row.index, row.values, label=f'Row {index}')
        if row['LABEL'] == 1:
            plt.plot(row.index, row.values, label=f'Row {index}, no planets', color='maroon')
        else:
            plt.plot(row.index, row.values, label=f'Row {index}, with orbitting planets', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Flux')
    plt.title('Flux Over Time')
    plt.xticks([])
    plt.legend()
    plt.show()
twoRRows()
