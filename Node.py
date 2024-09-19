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
    
def expand(current):
    successors = []
    state = current.getState()
    
    if(state['pos'][1] != 1):
        leftState = copyState(state)
        leftState['pos'][1] -= 1
        leftNode = Node(current, leftState, 'left', 1.0)
        successors.append(leftNode)
        
    if(state['pos'][1] != 5):
        rightState = copyState(state)
        rightState['pos'][1] += 1
        rightNode = Node(current, rightState, 'right', .9)
        successors.append(rightNode)
    
    if(state['pos'][0] != 1):
        upState = copyState(state)
        upState['pos'][0] -= 1
        upNode = Node(current, upState, 'up', .8)
        successors.append(upNode)
        
    if(state['pos'][0] != 4):
        downState = copyState(state)
        downState['pos'][0] += 1
        downNode = Node(current, downState, 'down', .7)
        successors.append(downNode)
        
    suckState = copyState(state)
    if(suckState['pos'] in suckState['dirt']):
        suckState['dirt'].remove(suckState['pos'])
    suckNode = Node(current, suckState, 'suck', .6)
    successors.append(suckNode)
    
    return successors

def copyState(state):
    newState = {}
    newState['pos'] = state['pos'].copy()
    newState['dirt'] = state['dirt'].copy()
    return newState
