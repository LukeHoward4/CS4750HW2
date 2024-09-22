from queue import PriorityQueue
from Node import Node, expand, calculate_path_cost

ACTION_COSTS = {
    'left': 1.0,
    'right': 0.9,
    'up': 0.8,
    'down': 0.7,
    'suck': 0.6
}

def goal_test(state):
    return len(state['dirt']) == 0

def uniform_cost_tree_search(problem):
    fringe = PriorityQueue()
    
    initial_node = Node(
        parentNode=None,
        state=problem['initial_state'],
        action=None,
        pathCost=0.0,
        depth=0
    )
    
    fringe.put((0, initial_node))

    while not fringe.empty():
        _, node = fringe.get()

        if goal_test(node.getState()):
            return construct_solution(node)  

        for child in expand(node):
            fringe.put((calculate_path_cost(child), child))

    return "Fail"  

def construct_solution(node):
    actions = []
    while node.get_parent() is not None:
        actions.append(node.getAction())  
        node = node.get_parent()          
    actions.reverse()  
    return actions

problem_instance_1 = {
    'initial_state': {'pos': [2, 2], 'dirt': [[1, 2], [2, 4], [3, 5]]},
    'grid_size': (4, 5)
}

solution_instance_1 = uniform_cost_tree_search(problem_instance_1)
print(f"Solution for instance 1: {solution_instance_1}")

problem_instance_2 = {
    'initial_state': {'pos': [3, 2], 'dirt': [[1, 2], [2, 1], [2, 4], [3, 3]]},
    'grid_size': (4, 5)
}

solution_instance_2 = uniform_cost_tree_search(problem_instance_2)
print(f"Solution for instance 2: {solution_instance_2}")

