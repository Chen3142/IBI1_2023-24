#import the pyplot from matplotlib and name it plt
import matplotlib.pyplot as plt
#make a dictionary and record the data
data = {
    'Sleeping': 8,
    'Classes': 6,
    'Studying': 3.5,
    'TV': 2,
    'Music': 1,
    'Other': 3.5 
}
#print the doctionary
print(data)

#construct a pie chart
labels = list(data.keys())
time_size= list(data.values())
explode = [0,0,0,0,0,0]
plt.figure()
plt.title('Time spent during an average day')#give the title
plt.pie(time_size, explode=explode,labels =labels,autopct='%1.1f%%')
plt.show()#show the chart
plt.clf() #close the chart

#remind the user to enter the activity name
activity = input("Please enter the activity name:")
#output activity time. If the activity name entered cannot be found, output tips. 
if activity in data:
    time_spent = data[activity]
    print(f"The average number of hours spent on {activity} is {time_spent} hour(s)") 
else:
    print("Sorry, this activity name could not be found.")