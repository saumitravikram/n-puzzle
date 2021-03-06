'''
Created on Jan 29, 2017

@author: saumitra
'''
from Board import Board 
from __builtin__ import True

class State(Board):
    '''
    This represent the state in state space search tree and to find all children/neighbour node
    '''

    def __init__(self,parent,boardConfig,move,cost):
        '''
        Constructor to initialize 
            Board Configuration
            Parent State
            Move ('Up'/'Down'/'Left'/'Right')
            Cost from root node
        '''
        self.parent=parent
        Board.__init__(self,boardConfig)
        self.move=move
        self.cost=cost
    
    #Return if current state is goal node or not
    def isGoal(self):
        goalState=self.GoalBoard()
        if cmp(goalState,self.boardConfig) == 0:
            return True
        else:
            return False
    
    #Return all possible child nodes/state from current state in order UDLR 
    def neighbour(self):
        newStates=[]
        if self.MoveUp()!=None:
            newStates.append(State(self,self.MoveUp(),'Up',self.cost+1))
        if self.MoveDown()!=None:
            newStates.append(State(self,self.MoveDown(),'Down',self.cost+1))
        if self.MoveLeft()!=None:
            newStates.append(State(self,self.MoveLeft(),'Left',self.cost+1))
        if self.MoveRight()!=None:
            newStates.append(State(self,self.MoveRight(),'Right',self.cost+1))
        return newStates
        