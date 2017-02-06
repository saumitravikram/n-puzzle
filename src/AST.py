'''
Created on Feb 4, 2017

@author: saumitra
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
        counter=0
        fringeList=[]
        fringeBoard=Set()
        explored=[]
        exploredBoard=Set()
        fringe.put((self.initialSate.cost+self.initialSate.h(),0,counter,self.initialSate))
        fringeList.append(self.initialSate)
        fringeBoard.add(self.initialSate.boardConfig)
        maxfringeSize=1
        maxSearchDepth=self.initialSate.cost
        while fringe:
            if len(fringeList) > maxfringeSize:
                maxfringeSize=len(fringeList)
            state=fringe.get()[3]
            fringeBoard.remove(state.boardConfig)
            fringeList.remove(state)
            explored.append(state)
            exploredBoard.add(state.boardConfig)
            if state.isGoal():
                result=Result(state,explored,fringeList,maxfringeSize,maxSearchDepth)
                return result
            for neighbour in state.neighbour():
                temp=compareState(neighbour.boardConfig,fringeBoard,exploredBoard)        
                if temp == False:
                    counter+=1
                    if neighbour.move == 'Up' :
                        fringe.put((neighbour.cost+neighbour.h(),0.1,counter,neighbour))
                    elif neighbour.move == 'Down':
                        fringe.put((neighbour.cost+neighbour.h(),0.2,counter,neighbour))
                    elif neighbour.move == 'Left':
                        fringe.put((neighbour.cost+neighbour.h(),0.3,counter,neighbour))
                    elif neighbour.move == 'Right':
                        fringe.put((neighbour.cost+neighbour.h(),0.4,counter,neighbour))
                    fringeBoard.add(neighbour.boardConfig)
                    fringeList.append(neighbour)
                    if neighbour.cost > maxSearchDepth :
                        maxSearchDepth = neighbour.cost

                    
            
        return None

        