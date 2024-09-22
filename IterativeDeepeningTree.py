import Node
import time

def iterativeDeepeningTreeSearch(startNode):
    start = time.time()
    limit = 0
    expanded = 0
    generated = 1
    firstFive = 1
    while(limit <= 16):
        fringe = [startNode]
        #Fringe begins at the starter node
        print('limit = ' + str(limit))
        #Tracking the limit so user knows that program is still running
        while(fringe):
            current = fringe[-1]
            #Pulling from the fringe using LIFO
            if(current.getDepth() < limit):
                #Only expand if expanded nodes will be at or below limit
                newNodes = Node.expand(current)
                expanded+=1
                if(firstFive <= 5):
                    #Recording the states of the first five expanded nodes.
                    print('State of node ' + str(firstFive) + ': ' + str(current.getState()))
                    firstFive+= 1
                for node in newNodes:
                    #Adding new nodes to generated
                    generated+=1
                    if(not node.getState()['dirt']):
                        #checking to see if goal state achieved
                        displayStats(start, generated, expanded)
                        return node
                    fringe.append(node)
                    
            fringe.remove(current)                  
        limit += 1
    displayStats(start, generated, expanded)
    return 0

def displayStats(start, generated, expanded):
        totalTime = time.time() - start
        print('time taken: ' + str(totalTime))
        print('total nodes generated: ' + str(generated))
        print('total nodes expanded: ' + str(expanded))
    
def main():
    firstState = {}
    firstState['pos'] = [2, 2]
    firstState['dirt'] = [[1, 2], [2, 4], [3, 5]]
    starterNode = Node.Node(None, firstState, None, 0, 0)
    returnVal = iterativeDeepeningTreeSearch(starterNode)
    if(type(returnVal) != int):
        print('path cost: ' + str(Node.calculate_path_cost(returnVal)))
        print(Node.findSequence(returnVal))
    else:
        print(returnVal)
    secondState = {}
    secondState['pos'] = [3, 2]
    secondState['dirt'] = [[1, 2], [2, 1], [2, 4], [3, 3]]
    starterNode = Node.Node(None, secondState, None, 0, 0)
    returnVal = iterativeDeepeningTreeSearch(starterNode)
    if(type(returnVal) != int):
        print('path cost: ' + str(Node.calculate_path_cost(returnVal)))
        print(Node.findSequence(returnVal))
    else:
        print(returnVal)
    

main()
