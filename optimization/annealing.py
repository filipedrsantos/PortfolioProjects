import numpy as np
import random
import math
from scipy.spatial.distance import cdist
import time

# Simulated Annealing Algorithm:
    # start from a random configuration. 
    # swap the order of the starting configuration in 2 random positions and compare the path distances.
    # if the new distance is smaller than the original distance then 
        # accept the new path with probability 1 and the best path distance is updated to this value
    # if the new distance is larger than the original distance then 
        # accept the new path with a probability that depends on the distance difference and current temperature (to avoid local minima)
    # run for a determined number of iterations until the temperature (which decreases with cooling_rate) becomes very small (ex: 10^-18)

# time_ini
start_time = time.time()

# n random points in 2D space
num_cities = 10000
np.random.seed(42)
points = 100*np.random.rand(num_cities, 2)
#print("points", points)

# Pairwise distance matrix
dist_matrix = cdist(points, points, metric='euclidean')

# Annealing function
def simulated_annealing(dist_matrix, initial_temperature=10000, cooling_rate=0.995, iterations=10000):
    
    # Chose a random initial path
    current_path = list(range(len(dist_matrix)))
    random.shuffle(current_path)

    # Calculate the total distance of the current path
    current_distance = total_distance(current_path, dist_matrix)

    # Initialize the best path
    best_path = current_path
    best_distance = current_distance

    # Annealing method
    temperature = initial_temperature
    for i in range(iterations):

        # Make a small change in the path (swap two points)
        new_path = current_path[:]
        swap_indices = random.sample(range(len(new_path)), 2) # Chose two random indices of the current permutation
        new_path[swap_indices[0]], new_path[swap_indices[1]] = new_path[swap_indices[1]], new_path[swap_indices[0]] # Swap those indices in the new permutation

        # Calculate the new distance
        new_distance = total_distance(new_path, dist_matrix)

        # Accept the new path (that is, it becomes the current path) if it has a lower distance, 
        # or accept the new path, even if the distance is larger, with a probability given by e^[(current_distance - new_distance)/temperature]
        # to avoid local minimum
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_path = new_path
            current_distance = new_distance

            # Update the best path if necessary
            if current_distance < best_distance:
                best_path = current_path
                best_distance = current_distance

        # Decrease the temperature so that progressivly becomes less likely to accept a path with a larger distance than the best found at the moment
        temperature *= cooling_rate #temperature = temperature*cooling_rate + temperature

        # Note: The hyoerparameters - initial temperature, cooling_rate and number of iterations are related. We want the final temperature to be very small 
        # so that the algorithm does not accept a path with larger distance than the best found. This temperautre is given by T_fin = T_ini*cooling_rate^N_ite,
        # and thus the number of iterations is given by N_ite = ln(T_fin/T_ini)/ln(cooling_rate).

    return best_path, best_distance

# Calculate total distance of a given path
def total_distance(path, dist_matrix):
    distance = 0
    for i in range(len(path) - 1):
        distance += dist_matrix[path[i], path[i + 1]]
    distance += dist_matrix[path[-1], path[0]]  # Add the distance between the last point and the starting point
    return distance

# Run the Annealing algorithm
best_path, best_distance = simulated_annealing(dist_matrix)

# Output the optimal (or near-optimal) path and its total distance
#print("Optimal path (indices of points):", best_path)
print("Total distance of the optimal path:", best_distance)

# Running time
print("--- %s seconds ---" % (time.time() - start_time))