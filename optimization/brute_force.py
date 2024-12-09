import numpy as np
from scipy.spatial.distance import cdist
from itertools import permutations
import time

# Brute Force Algorithm:
    # calculate the total distance of a certain path and save it as the best path if its distance is smaller than the minimum distance found so far
    # repeat for each permutation possible and find the minimum total distance 

# time_ini
start_time = time.time()

# n random points in 2D space
num_cities = 10
np.random.seed(42)
points = 100*np.random.rand(num_cities, 2)
#print("points", points)

# Pairwise distance matrix
dist_matrix = cdist(points, points, metric='euclidean')

# Brute Force Algorithm: calculate the total distance for each permutation possible (n!). 
# For 10! = 3.628.800 we can use brute force, but for 20! = 2.43e+18 is impossible to solve using this method

def brute_force(dist_matrix):

    min_distance = float('inf') # initialization distance (infinite)
    best_path = None # initialization path

    for perm in permutations(range(len(points))):
        # Calculate the distance for this permutation
        distance = 0 # initialization distance
        for i in range(len(perm) - 1):
            distance += dist_matrix[perm[i], perm[i + 1]] # "+=" is equivalent to (distance = dist_matrix + distance)
        # Add the distance from the last point to the starting point
        distance += dist_matrix[perm[-1], perm[0]]
        
        # Compare the distance of path "i" with the minimum distance among the previous calculated path distances (min_distance)  
        # Update it as the best path if the distance is lower than min_distance
        if distance < min_distance:
            min_distance = distance
            best_path = perm

    return best_path, min_distance
 
# Run the brute force algorithm
best_path, min_distance = brute_force(dist_matrix)

# Output the optimal path and its total distance
print("Optimal path (indices of points):", best_path)
print("Total distance of the optimal path:", min_distance)

# Running time
print("--- %s seconds ---" % (time.time() - start_time)) # less than 6 seconds for n = 10.