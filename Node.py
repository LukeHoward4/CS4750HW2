class Node():
    def __init__(self, parentNode, state, action, pathCost):
        self.__parentNode = parentNode
        self.__state = state
        self.__action = action
        self.__pathCost = pathCost
    
