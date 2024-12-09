import numpy as np
from scipy.spatial.distance import cdist
import time

# Branch and Bound Algorithm:
    # Chose a starting point, ex: A, reduce the distance matrix and calculate the reduction cost (cost of leaving A)
    # Apply a recursion and backtrack algorithm: (check branch_search)
        # visit the next not visited location, ex: B 
        # apply contrains to the reduced matrix so that the path A - B is settled
        # reduce the matrix again and calculate the cost of going from A to B plus the cost of leaving B
        # sum this cost to the current cost (cost of leaving A)
        # if the new current cost is larger than the minimun total cost found so far (bound), stop searching this path (prune the path)
        # otherwise apply recursion (level = level + 1) and keep searching this path (ex: A - B - C), reduce and constrain the matrix and calculate further costs
        # repeat until the path is pruned or completes (level = number of locations), 
        # if it completes, add the cost of going back to the starting point and save the total_distance as the new bound
        # after a branch is completed, apply backtrack to explore other paths
    # The last saved path will be the best path.

# time_ini
start_time = time.time()

# Generates random locations and the distance matrix
def generate_data(num_cities, seed=42):
    np.random.seed(seed)
    points = 100 * np.random.rand(num_cities, 2)  # n random points in 2D space
    dist_matrix = cdist(points, points, metric='euclidean')  # Pairwise distance matrix
    np.fill_diagonal(dist_matrix, float('inf'))  # Set diagonal to +inf, instead of 0, to avoid self-loops
    return points, dist_matrix

# Function to reduce rows and columns, and calculate the reduction cost
def reduce_matrix(cost_matrix):
    """Performs row and column reductions, returning the reduced matrix and the reduction cost"""
    num_cities = cost_matrix.shape[0]
    reduction_cost = 0

    # Row reduction
    for i in range(num_cities):
        row_min = np.min(cost_matrix[i, :])
        if row_min < float('inf'):  # Avoid reducing rows with all infinities
            cost_matrix[i, :] -= row_min
            reduction_cost += row_min

    # Column reduction
    for j in range(num_cities):
        col_min = np.min(cost_matrix[:, j])
        if col_min < float('inf'):  # Avoid reducing columns with all infinities
            cost_matrix[:, j] -= col_min
            reduction_cost += col_min

    return cost_matrix, reduction_cost

# Function to update the matrix when a path is selected
def apply_path_constraints(cost_matrix, from_city, to_city):
    """Sets constraints for the Branch and Bound algorithm."""
    
    # Remove the row of the departing city
    cost_matrix[from_city, :] = float('inf')
    
    # Remove the column of the arriving city
    cost_matrix[:, to_city] = float('inf')
    
    # Prevent returning to the starting city
    cost_matrix[to_city, from_city] = float('inf')
    
    return cost_matrix

# Recursive function to solve TSP using Branch and Bound
def branch_and_bound_tsp(cost_matrix, current_bound, current_path, level, visited): # cost_matrix = reduced_matrix, current_bound = reduction_cost, current_path = starting point
    """Recursive implementation of Branch and Bound for TSP."""
    global best_cost, best_path

    num_cities = cost_matrix.shape[0]

    # If all cities are visited, complete the path back to the starting city
    if level == num_cities:
        # Add cost of returning to the starting city
        return_to_start_cost = cost_matrix[current_path[-1], current_path[0]]
        total_cost = current_bound + return_to_start_cost # No need to add the reduction_cost because the cost of leaving the last location is always 0
        if total_cost < best_cost:
            best_cost = total_cost
            best_path = current_path[:]
        return

    # Explore all possible next cities
    for next_city in range(num_cities):
        if not visited[next_city]:
            # Copy the current cost matrix and apply constraints
            temp_matrix = cost_matrix.copy() #reduced_matrix
            temp_matrix = apply_path_constraints(temp_matrix, current_path[-1], next_city)

            # Reduce the matrix and calculate the new lower bound
            reduced_matrix, reduction_cost = reduce_matrix(temp_matrix)
            new_bound = current_bound + cost_matrix[current_path[-1], next_city] + reduction_cost

            # If the new bound is better than the best known cost, continue
            if new_bound < best_cost:
                visited[next_city] = True
                current_path.append(next_city)

                branch_and_bound_tsp(reduced_matrix, new_bound, current_path, level + 1, visited)

                # Backtrack
                visited[next_city] = False
                current_path.pop() #removes the last city from the current_path

# Main function to solve TSP using Branch and Bound
def solve_tsp(cost_matrix):
    """Solves the TSP using Branch and Bound."""
    global best_cost, best_path
    num_cities = cost_matrix.shape[0]
    starting_city = 0

    # Initial reduction
    reduced_matrix, reduction_cost = reduce_matrix(cost_matrix.copy())
    current_bound = reduction_cost

    # Initialize variables
    best_cost = float('inf') 
    best_path = []

    # Start recursive branching
    visited = [False] * num_cities
    visited[starting_city] = True
    branch_and_bound_tsp(reduced_matrix, current_bound, [starting_city], 1, visited)

    return best_cost, best_path

# Example Usage
if __name__ == "__main__":
    
    num_cities = 10  # Number of cities
    points, cost_matrix = generate_data(num_cities)  # Generate points and cost matrix
    
    # # Example cost matrix (symmetric TSP)
    # cost_matrix = np.array([
    #     [float('inf'), 10, 15, 20],
    #     [10, float('inf'), 35, 25],
    #     [15, 35, float('inf'), 30],
    #     [20, 25, 30, float('inf')]
    # ])

    # Solve the TSP
    best_cost, best_path = solve_tsp(cost_matrix)

    print("Optimal Cost:", best_cost)
    print("Optimal Path:", best_path)

    # Running time
    print("--- %s seconds ---" % (time.time() - start_time))