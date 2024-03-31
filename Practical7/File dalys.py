#import a few python libraries and name them.
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#change the working directory to the file is stored.
os.chdir("\桌面\IBI\IBI1_2023-24\Practical7")

#read the content of the .csv file and name it.
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")

#show the fourth column from every 10th row, from 1st to 100th(inclusive)
every10row=dalys_data.iloc[0:100:10,3]
print(every10row)

#show DALYs for all rows corresponding to Afghanistan
Entity_is_Afghanistan=dalys_data.loc[:, "Entity"] == 'Afghanistan'
Afghanistan=dalys_data.loc[Entity_is_Afghanistan,"DALYs"]
print(Afghanistan)

#calculate the mean of DALYs in China.
china_data = dalys_data[dalys_data['Entity'] == 'China']
average_DALYs = np.mean(china_data['DALYs'])
print("The mean of DALYs in China is",average_DALYs)

#compare the mean with the data of 2019.
DALYs_of_2019=22270.51
print("DALYs in China for 2019:", DALYs_of_2019)
if average_DALYs > DALYs_of_2019:
    print("The DALYs of 2019 was below the mean."),
elif average_DALYs < DALYs_of_2019:
    print("The DALYs of 2019 was above the mean.")

# created a plot showing the DALYS over time in China
china_data_Years, china_data_DALYs = china_data['Year'].values, china_data['DALYs'].values
plt.plot(china_data_Years, china_data_DALYs, 'b+')
plt.xticks(china_data_Years,rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Over Years in China')
plt.show()
plt.clf()

#creat a bar chart of the Canada's DLAYs over time.
canada_data = dalys_data[dalys_data['Entity'] == 'Canada']
canada_data_Years, canada_data_DALYs = canada_data['Year'].values, canada_data['DALYs'].values
plt.bar(canada_data_Years,canada_data_DALYs)
plt.xlabel('Year')
plt.ylabel('DLAYs')
plt.title('The DLAYs of Canada over time')
plt.show()
plt.clf()