import heapq
import time
from Node import Node, calculate_path_cost, expand  


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, node, priority):
        heapq.heappush(self.elements, (priority, node))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def uniform_cost_graph_search(initial_state):
    closed = set()
    fringe = PriorityQueue()
    
    initial_node = Node(None, initial_state, None, 0, 0)
    
    fringe.put(initial_node, 0)
    
    start_time = time.time()
    
    expanded_count = 0
    generated_count = 1  
    
    while not fringe.empty():
        current_node = fringe.get()
        
        if not current_node.getState()['dirt']: 
            end_time = time.time()
            execution_time = end_time - start_time
            solution, solution_cost = reconstruct_solution(current_node)
            return {
                "solution": solution,
                "cost": solution_cost,
                "moves": len(solution),
                "expanded": expanded_count,
                "generated": generated_count,
                "time": execution_time
            }
        
        # Checking the state by the position of the agent and the dirt
        state_tuple = (tuple(current_node.getState()['pos']), tuple(tuple(dirt) for dirt in current_node.getState()['dirt']))

        # Checking if the state has been visited before, if no then expanding it
        if state_tuple not in closed:
            closed.add(state_tuple)  
            expanded_count += 1  # We are expanding this node
            
            # Expand the node and add its children to the priority queue
            for child in expand(current_node):  
                generated_count += 1  
                fringe.put(child, child.get_path_cost())  # Insert child into the fringe based on its path cost
    
    return None 

# Reconstruct the solution path from the goal node
def reconstruct_solution(node):
    actions = []
    total_cost = 0
    while node.get_parent() is not None:
        actions.append(node.getAction())
        total_cost += node.get_path_cost()
        node = node.get_parent()
    actions.reverse()
    return actions, total_cost

initial_state_1 = {
    'pos': [2, 2],
    'dirt': [[1, 2], [2, 4], [3, 5]]
}

initial_state_2 = {
    'pos': [3, 2],
    'dirt': [[1, 2], [2, 1], [2, 4], [3, 3]]
}

result_1 = uniform_cost_graph_search(initial_state_1)
result_2 = uniform_cost_graph_search(initial_state_2)

print("Instance #1 Result:", result_1)
print("Instance #2 Result:", result_2)
