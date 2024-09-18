class Node():
    def __init__(self, parentNode, state, action, pathCost):
        self.__parentNode = parentNode
        self.__state = state
        self.__action = action
        self.__pathCost = pathCost

    def get_parent(self):
        return self.__parentNode

    def get_path_cost(self):
        return self.__pathCost

def calculate_path_cost(node):
    total_cost = 0
    while node is not None:
        total_cost += node.get_path_cost()
        node = node.get_parent()
    return total_cost
    
