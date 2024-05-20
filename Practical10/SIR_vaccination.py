#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#define the variables
N = 10000 #the total number of people
infected_start = 1 # Infected
recovered_start = 0 # Recovered
vaccinated_rates = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #vaccination rate

for vaccinated_rate in vaccinated_rates:
    vaccinated = int(vaccinated_rate * N)  # Vaccinated
    susceptible_start = N - infected_start - recovered_start - vaccinated  # Susceptible
    
    beta = 0.3 # Transmission rate
    gamma = 0.05 # Recovery rate

    # create arrays for variables
    susceptible = [susceptible_start]
    infected = [infected_start]
    recovered = [recovered_start]


    for _ in range(1000):
       #need to know the recovery probability for each infected individual and the probability of infection.
       i=beta * infected[-1] / N #infection probability
       r=gamma #recovery probability
       i=min(max(i,0),1)
       r=min(max(r,0),1)
     
       susceptible_now=susceptible[-1]
       infected_now=infected[-1]
       recovered_now=recovered[-1]

       # choose randomly infected and recovered
       if susceptible_now>0:
          infected_choose = np.random.choice([0, 1], size=susceptible[-1], p=[1 - i, i])
          infected_new = np.sum(infected_choose)
       else:
          infected_new = 0
    
       if infected_now>0:
          recovered_choose = np.random.choice([0, 1], size=infected[-1], p=[1 - r, r])
          recovered_new = np.sum(recovered_choose)
       else:
          recovered_new = 0
          
       susceptible_now=max(susceptible[-1] - infected_new,0)
       infected_now=max(infected[-1] + infected_new - recovered_new,0)
       recovered_now=max(recovered[-1] + recovered_new,0)

       #keep track of the numbers of susceptible, infected and recovered.
       susceptible.append(susceptible_now)
       infected.append(infected_now)
       recovered.append(recovered_now)
    # plot
    plt.plot(infected, label=f"{vaccinated_rate*100}%")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vacation rates")
plt.legend()
plt.show()
plt.clf()