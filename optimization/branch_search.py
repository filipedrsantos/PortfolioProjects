
# Branch Search: understand recursion + backtrack
    # ignores the costs and matrix modifications
    # adds prints to help understand the branching and bactrackig process

def branch_and_bound_tsp_simple(current_path, level, visited):
    """Simplified version of Branch and Bound for TSP (ignoring costs and matrix reductions)."""
    
    num_cities = len(visited)
    print(f"Level_Start {level}")
    # Base case: all cities visited
    if level == num_cities:
        print(f"Level_Complete {level}")
        print(f"Complete path: {current_path}")
        return
    
    # Explore all possible next cities
    for next_city in range(num_cities):
        print(f"n = {next_city}")
        if not visited[next_city]:
            # Mark this city as visited and add it to the current path
            visited[next_city] = True
            current_path.append(next_city)
            
            # Print current state
            print(f"Level {level}, visiting city {next_city}, current path: {current_path}")
            
            # Recurse to the next level
            branch_and_bound_tsp_simple(current_path, level + 1, visited)
            
            # Backtrack: unmark the city and remove it from the path
            print(f"Level_Back {level}")
            visited[next_city] = False
            current_path.pop()
            
            # Print the state after backtracking
            print(f"Backtracked from city {next_city}, current path: {current_path}")

# Main function to start the search
def solve_tsp_simple(num_cities):
    """Solve the TSP problem (simplified version)."""
    visited = [False] * num_cities
    current_path = []
    
    # Start from city 0
    visited[0] = True
    current_path.append(0)
    
    # Start recursive branching
    branch_and_bound_tsp_simple(current_path, 1, visited)

# Run the simplified version with 4 cities
solve_tsp_simple(4)
