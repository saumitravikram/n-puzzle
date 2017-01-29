'''
Created on Jan 29, 2017

@author: saumitra
'''
from Board import Board 
from __builtin__ import True

class State(Board):
    '''
    This represent the state in state space search
    '''

    def __init__(self,parent,boardConfig,move):
        '''
        Constructor
        '''
        self.parent=parent
        Board.__init__(self,boardConfig)
        self.move=move
    
    #Return if current state is goal node or not
    def isGoal(self):
        goalState=self.GoalBoard()
        if goalState==self.boardConfig:
            return True
        else:
            return False
        
    def neighbour(self):
        newStates=[]
        if self.MoveUp()!=None:
            newStates.append(State(self,self.MoveUp(),'Up'))
        if self.MoveDown()!=None:
            newStates.append(State(self,self.MoveDown(),'Down'))
        if self.MoveLeft()!=None:
            newStates.append(State(self,self.MoveLeft(),'Left'))
        if self.MoveRight()!=None:
            newStates.append(State(self,self.MoveRight(),'Right'))
        return newStates
        