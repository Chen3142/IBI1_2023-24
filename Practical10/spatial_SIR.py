#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Create an array representing the population, with all susceptible individuals(0).
population = np.zeros((100, 100))

# Randomly select a point for the initial outbreak with infected(1).
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Define model parameters
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate

# Total time points to simulate
time_points = 100

# Specific time points to plot
times_to_plot = [0, 10, 50, 100]
plot_index = 1

# Loop for each time point
for t in range(time_points + 1):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop for all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?)
        for xNeighbour in range(x-1,x+2):
           for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?) :Yes, avoidance of repetition
            if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                    if population[xNeighbour,yNeighbour]==0:
                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]

        # Infected individuals will recover
        if np.random.random() < gamma:
            population[x, y] = 2  # Recover

    
    # Plot the specified time points
    if t in times_to_plot:
        #Use subgraphs to display four graphs at once
        plt.subplot(2, 2, plot_index)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time: {t}")
        plot_index += 1

# Automatically adjust the subplot layout to avoid overlap
plt.tight_layout()
plt.show()
plt.clf()
