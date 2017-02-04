'''
Created on Feb 4, 2017

@author: saumitv
'''

from Queue import PriorityQueue
from sets import Set
from Utlis import compareState
from Result import Result 


class AST():
    '''
    Search state space tree using Breadth First Search
    '''
    
    def __init__(self,initialState):
        '''
        Constructor
        '''
        self.initialSate=initialState

    #Algorithm for BFS to search
    def searchAlgo(self):
        fringe=PriorityQueue()
        fringeList=[]
        fringeBoard=Set()
        explored=[]
        exploredBoard=Set()
        g=0
        fringe.put((g+self.initialSate.h(),self.initialSate))
        fringeList.append(self.initialSate)
        fringeBoard.add(self.initialSate.boardConfig)
        maxfringeSize=1
        maxSearchDepth=self.initialSate.cost
        while fringe:
            if len(fringeList) > maxfringeSize:
                maxfringeSize=len(fringeList)
            state=fringe.get()[1]
            fringeBoard.remove(state.boardConfig)
            fringeList.remove(state)
            explored.append(state)
            exploredBoard.add(state.boardConfig)
            if state.isGoal():
                result=Result(state,explored,fringeList,maxfringeSize,maxSearchDepth)
                return result
            g+=1
            for neighbour in state.neighbour():
                temp=compareState(neighbour.boardConfig,fringeBoard,exploredBoard)
                if temp == False:  
                    fringe.put((g+neighbour.h(),neighbour))
                    fringeBoard.add(neighbour.boardConfig)
                    fringeList.append(neighbour)
                    if neighbour.cost > maxSearchDepth :
                        maxSearchDepth = neighbour.cost
        return None

        