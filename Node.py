class Node():
    def __init__(self, parentNode, state, action, pathCost, depth):
        self.__parentNode = parentNode
        self.__state = state
        self.__action = action
        self.__pathCost = pathCost
        self.__depth = depth

    def get_parent(self):
        return self.__parentNode
    def get_path_cost(self):
        return self.__pathCost
    def getState(self):
        return self.__state
    def getAction(self):
        return self.__action
    def getDepth(self):
        return self.__depth
    
def calculate_path_cost(node):
    total_cost = 0
    while node is not None:
        total_cost += node.get_path_cost()
        node = node.get_parent()
    return total_cost
    
def expand(current):
    successors = []
    state = current.getState()
    depth = current.getDepth() + 1
    if(state['pos'][1] != 1):
        leftState = copyState(state)
        leftState['pos'][1] -= 1
        leftNode = Node(current, leftState, 'left', 1.0, depth)
        successors.append(leftNode)
        
    if(state['pos'][1] != 5):
        rightState = copyState(state)
        rightState['pos'][1] += 1
        rightNode = Node(current, rightState, 'right', .9, depth)
        successors.append(rightNode)
    
    if(state['pos'][0] != 1):
        upState = copyState(state)
        upState['pos'][0] -= 1
        upNode = Node(current, upState, 'up', .8, depth)
        successors.append(upNode)
        
    if(state['pos'][0] != 4):
        downState = copyState(state)
        downState['pos'][0] += 1
        downNode = Node(current, downState, 'down', .7, depth)
        successors.append(downNode)
        
    suckState = copyState(state)
    if(suckState['pos'] in suckState['dirt']):
        suckState['dirt'].remove(suckState['pos'])
    suckNode = Node(current, suckState, 'suck', .6, depth)
    successors.append(suckNode)
    
    return successors

def copyState(state):
    newState = {}
    newState['pos'] = state['pos'].copy()
    newState['dirt'] = state['dirt'].copy()
    return newState



