import time
from queue import PriorityQueue
from Node import Node, expand, calculate_path_cost

ACTION_COSTS = {
    'left': 1.0,
    'right': 0.9,
    'up': 0.8,
    'down': 0.7,
    'suck': 0.6
}

#Are rooms cleaned?
def goal_test(state):
    return len(state['dirt']) == 0

def state_to_tuple(state):
    return (tuple(state['pos']), tuple([tuple(dirt) for dirt in state['dirt']]))


def uniform_cost_graph_search(problem):
    start_time = time.time()  
    generated_nodes = 0
    expanded_nodes = 0
    first_five_expanded = []

    fringe = PriorityQueue()
    visited = set()

    initial_node = Node(
        parentNode=None,
        state=problem['initial_state'],
        action=None,
        pathCost=0.0,
        depth=0
    )
#Add node into fringe
    fringe.put((0, initial_node))
    visited.add(state_to_tuple(initial_node.getState()))  
    generated_nodes += 1

    while not fringe.empty():
        _, node = fringe.get()
        expanded_nodes += 1

        if expanded_nodes <= 5:
            first_five_expanded.append(node.getState())

        if goal_test(node.getState()):
            end_time = time.time()  
            return construct_solution(node, generated_nodes, expanded_nodes, calculate_path_cost(node), end_time - start_time, first_five_expanded)

        for child in expand(node):
            child_state_tuple = state_to_tuple(child.getState())

            if child_state_tuple not in visited:
                fringe.put((calculate_path_cost(child), child))
                visited.add(child_state_tuple)
                generated_nodes += 1

    return "Fail"  # Return failure if no solution is found

# makes the solution from the goal node by tracing back the parent nodes
def construct_solution(node, generated_nodes, expanded_nodes, path_cost, time_taken, first_five_expanded):
    actions = []
    while node.get_parent() is not None:
        actions.append(node.getAction()) 
        node = node.get_parent()          
    actions.reverse()  

    print("First 5 expanded Nodes:")
    for i, state in enumerate(first_five_expanded, start=1):
        print(f"State of node {i}: {state}")

    # Used chatgpt to help display  solution details
    print(f"Solution: {actions}")
    print(f"Moves: {len(actions)}")
    print(f"Nodes generated: {generated_nodes}")
    print(f"Nodes expanded: {expanded_nodes}")
    print(f"Path cost: {path_cost}")
    print(f"Time taken: {time_taken:.3f} seconds")

    return actions


#INSTANCES
problem_instance_1 = {
    'initial_state': {'pos': [2, 2], 'dirt': [[1, 2], [2, 4], [3, 5]]},
    'grid_size': (4, 5)
}

solution_instance_1 = uniform_cost_graph_search(problem_instance_1)

problem_instance_2 = {
    'initial_state': {'pos': [3, 2], 'dirt': [[1, 2], [2, 1], [2, 4], [3, 3]]},
    'grid_size': (4, 5)
}

solution_instance_2 = uniform_cost_graph_search(problem_instance_2)
