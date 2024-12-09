import numpy as np
from scipy.spatial.distance import cdist
import time

# Nearest Neighbor Heuristic: 
    # start from a location, connect it to the closest neighbor location that was not visited yet and save the respective distance
    # repeat until all locations are visited, adding in each step the respective distance to the total distance
    # connect the last visited location to the starting location and calculate the final total distance

# Cons: 
    # may not give the exact solution
    # may not give a very good approximated solution (in the worst case it gives a distance 2 times larger than the optimal distance, assuming triangle inequality)

# Pros:
    # very fast (10000 points: 8 seconds)
    # may serve as starting path for methods such as the simulated annealing (check annealing_nn_path_ini)
    # may serve as a upper bound (distance) for methods such as branch and bound
    # may serve as a upper bound (time) for predicted time required for the travelling  

# Generates random locations and the distance matrix
def generate_data(num_cities, seed=42):
    np.random.seed(seed)
    points = 100 * np.random.rand(num_cities, 2)
    dist_matrix = cdist(points, points, metric='euclidean')
    return points, dist_matrix

# Generates data for the branch and bound method
def generate_data_bb(num_cities, seed=42):
    np.random.seed(seed)
    points = 100 * np.random.rand(num_cities, 2)  # n random points in 2D space
    dist_matrix = cdist(points, points, metric='euclidean')  # Pairwise distance matrix
    np.fill_diagonal(dist_matrix, float('inf'))  # Set diagonal to +inf, instead of 0, to avoid self-loops
    return points, dist_matrix

def nearest_neighbor_tsp(num_cities, dist_matrix, starting_city):

    # time_ini
    start_time = time.time()
    
    visited = [False] * num_cities
    path = [starting_city]  # Start at the first city 
    visited[starting_city] = True # Start at the first city
    total_distance = 0

    current_city = starting_city
    for _ in range(num_cities - 1):
        # Find the nearest unvisited city
        nearest_city = None
        nearest_distance = float("inf")
        for next_city in range(num_cities):
            if not visited[next_city] and dist_matrix[current_city, next_city] < nearest_distance:
                nearest_city = next_city
                nearest_distance = dist_matrix[current_city, next_city]
        
        # Visit the nearest city
        path.append(nearest_city)
        visited[nearest_city] = True
        total_distance += nearest_distance
        current_city = nearest_city

    # Return to the starting city
    total_distance += dist_matrix[current_city, path[0]]
    #path.append(path[0])

    # Running time
    print("--- %s seconds ---" % (time.time() - start_time))

    return path, total_distance

# Standalone execution
if __name__ == "__main__":
    num_cities = 10  # Number of points
    #starting_city = random.choice(list(range(num_cities)))
    starting_city = 0
    points, dist_matrix, = generate_data(num_cities)
    
    # number_of_tries = 10
    # for tries in range(number_of_tries):

    #print("Points:", points)

    path, total_distance = nearest_neighbor_tsp(num_cities, dist_matrix, starting_city)

    print("Nearest-Neighbor Path:", path)
    print("Total Distance:", total_distance)