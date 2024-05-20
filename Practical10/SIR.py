#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#define the variables
N = 10000 #the total number of people
infected_start = 1 # Infected
recovered_start = 0 # Recovered
susceptible_start = N - infected_start - recovered_start # Susceptible
beta = 0.3 # Transmission rate
gamma = 0.05 # Recovery rate

# create arrays for variables
susceptible = [susceptible_start]
infected = [infected_start]
recovered = [recovered_start]

# time loop
for _ in range(1000):
    #need to know the recovery probability for each infected individual and the probability of infection.
    i=beta * infected[-1] / N #infection probability
    r=gamma #recovery probability
    
    # choose randomly infected and recovered
    infected_choose = np.random.choice([0, 1], size=susceptible[-1], p=[1 - i, i])
    infected_new = np.sum(infected_choose)
    
    recovered_choose = np.random.choice([0, 1], size=infected[-1], p=[1 - r, r])
    recovered_new = np.sum(recovered_choose)
    
    #keep track of the numbers of susceptible, infected and recovered.
    susceptible.append(susceptible[-1] - infected_new)
    infected.append(infected[-1] + infected_new - recovered_new)
    recovered.append(recovered[-1] + recovered_new)

# plot
plt.figure(figsize =(6 ,4) , dpi=150)
plt.plot(susceptible, label="susceptible")
plt.plot(infected, label="infected")
plt.plot(recovered, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.show()
plt.clf()