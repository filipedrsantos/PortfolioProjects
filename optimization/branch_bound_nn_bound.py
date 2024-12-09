import numpy as np
from nn_heuristic import generate_data_bb, nearest_neighbor_tsp
import time

# Branch and Bound Algorithm using as upper bound the path distance calculated in the Nearest Neighbor Heuristic (instead of +inf)
# This made the algorithm considerably faster. For n=15, it went from 60 sec to 18 sec (3 times lower for just 15 points)

# time_ini
start_time = time.time()

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
    #best_cost = float('inf')
    best_cost = nn_total_distance
    best_path = []

    # Start recursive branching
    visited = [False] * num_cities
    visited[starting_city] = True
    branch_and_bound_tsp(reduced_matrix, current_bound, [starting_city], 1, visited)

    return best_cost, best_path

# Example Usage
if __name__ == "__main__":

    starting_city = 0
    num_cities = 10  # Number of cities
    points, cost_matrix = generate_data_bb(num_cities)  # Generate points and cost matrix

    nn_path, nn_total_distance = nearest_neighbor_tsp(num_cities, cost_matrix, starting_city)
    
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