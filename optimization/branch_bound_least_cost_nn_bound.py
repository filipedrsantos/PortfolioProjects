import numpy as np
from nn_heuristic import generate_data_bb, nearest_neighbor_tsp
import time
import heapq

# Lest Cost Branch and Bound Algorithm (LCBB):
    # chose a starting point, ex: A, reduce the distance matrix and calculate the reduction cost (cost of leaving A)
    # construct a priority queque for the branches (ordered by the cost) and add the branch with the starting point to the queque
    # while there is any branch in the queque:
        # select and branch out the current best branch. i.e, the top branch in the queque (at first will be A - B, then A - C...)
        # if the new branch cost is lower than the best cost found so far (initialized as +inf or a specific bounding)
            # save the new branch in the queque (in a position accordingly to the relative cost to other saved branches)
            # save the respective reduced matrix and make level = level + 1
        # if level == number of points (completed path) and the branch cost is lower than the best cost found do far, accpet this as the best current path
        # if a branch cost is worse than the best cost found so far, prune the branch

# Pros:
    # LCBB explores the tree in a more efficient way than BB
    # It creates an ordered queque and explores the branches that are more "promising" to lead up to the best path

#Cons:
    # Keeping a queque uses more memory



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

import heapq
import numpy as np

def least_cost_branch_and_bound_tsp(cost_matrix):
    
    global best_cost, best_path
    num_cities = cost_matrix.shape[0]

    # Initial reduction of the matrix
    initial_matrix, initial_reduction_cost = reduce_matrix(cost_matrix)
    initial_node = (initial_reduction_cost, [0], [True] + [False] * (num_cities - 1), initial_matrix, 1)
    
    # Priority queue for branches
    pq = []
    heapq.heappush(pq, initial_node)
    
    #best_cost = float('inf')
    best_cost = nn_total_distance
    best_path = []

    while pq:
        current_bound, current_path, visited, current_matrix, level = heapq.heappop(pq)
        #print(f"Processing node: Path = {current_path}, Bound = {current_bound}")

        # Prune branches with a bound worse than the best cost
        if current_bound >= best_cost:
            #print(f"Pruned node: Path = {current_path}, Bound = {current_bound}")
            continue

        # If all cities are visited, complete the cycle
        if level == num_cities:
            #print(f"Found complete path: {best_path}, Cost = {best_cost}")
            total_cost = current_bound + current_matrix[current_path[-1], current_path[0]]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = current_path + [current_path[0]]
                #print(f"Found complete path: {best_path}, Cost = {best_cost}")
            continue

        # Branch to all unvisited cities
        last_city = current_path[-1]
        for next_city in range(num_cities):
            if not visited[next_city]:
                # Copy and update the cost matrix
                temp_matrix = current_matrix.copy()
                temp_matrix = apply_path_constraints(temp_matrix, last_city, next_city)
                
                # Reduce the matrix and calculate the new bound
                reduced_matrix, reduction_cost = reduce_matrix(temp_matrix)
                new_bound = current_bound + current_matrix[last_city, next_city] + reduction_cost

                # If the new bound is promising, push the child node into the queue
                if new_bound < best_cost:
                    new_path = current_path + [next_city]
                    new_visited = visited[:]
                    new_visited[next_city] = True
                    heapq.heappush(pq, (new_bound, new_path, new_visited, reduced_matrix, level + 1))
                    #print(f"Added child: Path = {new_path}, Bound = {new_bound}")
    
    return best_cost, best_path


# Example Usage
if __name__ == "__main__":

    starting_city = 0
    num_cities = 10  # Number of cities
    points, cost_matrix = generate_data_bb(num_cities)  # Generate points and cost matrix

    nn_path, nn_total_distance = nearest_neighbor_tsp(num_cities, cost_matrix, starting_city)

    # Solve the TSP
    best_cost, best_path = least_cost_branch_and_bound_tsp(cost_matrix)

    print("Optimal Cost:", best_cost)
    print("Optimal Path:", best_path)

    # Running time
    print("--- %s seconds ---" % (time.time() - start_time))