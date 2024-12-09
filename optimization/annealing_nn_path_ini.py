import numpy as np
import random
import math
from scipy.spatial.distance import cdist
import time
from nn_heuristic import generate_data, nearest_neighbor_tsp

# Algorithm for the Simulated Annealing method
# Uses as starting path, the path calculated in the Nearest Neighbor Algorithm

num_cities = 30
#starting_city = random.choice(list(range(num_cities)))
starting_city = 9
points, dist_matrix = generate_data(num_cities)

print(points)

nn_path, nn_total_distance = nearest_neighbor_tsp(num_cities, dist_matrix, starting_city)

#print("Points", points)
print("Nearest-Neighbor Path:", nn_path)
print("Total Distance:", nn_total_distance)

# Calculate total distance of a given path
def total_distance(path, dist_matrix):
    distance = 0
    for i in range(len(path) - 1):
        distance += dist_matrix[path[i], path[i + 1]]
    distance += dist_matrix[path[-1], path[0]]  # Add the distance between the last point and the starting point
    return distance

current_path = nn_path
current_distance = nn_total_distance

# # Chose a random initial path
# current_path = list(range(len(dist_matrix)))
# random.shuffle(current_path)

# # Calculate the total distance of the current path
# current_distance = total_distance(current_path, dist_matrix)

# Annealing function
def simulated_annealing(current_path, current_distance, dist_matrix, initial_temperature=10000, cooling_rate=0.9995, iterations=100000):

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

# Run the Annealing algorithm
number_of_tries = 10

for tries in range(number_of_tries):
    
    # time_ini
    start_time = time.time()

    #print(current_path)
    best_path, best_distance = simulated_annealing(current_path, current_distance, dist_matrix)

    # Output the optimal (or near-optimal) path and its total distance
    #print("Optimal path (indices of points):", best_path)
    print("Total distance of the optimal path:", best_distance)

    # Running time
    print("--- %s seconds ---" % (time.time() - start_time))