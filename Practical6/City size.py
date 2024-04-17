#import the pyplot from matplotlib and name it plt
import matplotlib.pyplot as plt

#make two dictionaries to record data
uk_cities={
    'Stirling':0.04,
    'Edinburgh':0.56,
    'Glasgow':0.62,
    'London':9.7
}

china_cities={
    'Haining':0.58,
    'Hangzhou':8.4,
    'Beijing':22.2,
    'Shanghai':29.9
}
#print the dictionary    
print(uk_cities,china_cities)

#Resize images
plt.figure(figsize=(10, 5))

#make the first bar
plt.subplot(1, 2, 1) 
plt.bar(list(uk_cities.keys()), list(uk_cities.values()), color='blue')
plt.title('Populations of cities in the UK in 2024(millions)')
plt.xlabel('The UK city name')
plt.ylabel('Populations')

#make the second bar
plt.subplot(1, 2, 2)
plt.bar(list(china_cities.keys()), list(china_cities.values()), color='red')
plt.title('Populations of cities in China in 2024(millions)')
plt.xlabel('China city name')
plt.ylabel('Populations')

#layout adjustment
plt.tight_layout
plt.show()#show the chart
plt.clf()#close the chart