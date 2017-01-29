'''
Created on Jan 29, 2017

@author: saumitra
'''
import math
from Utlis import swap

class Board:
    '''
    This class represent N-puzzle board and functions to move tiles and print board
    '''


    def __init__(self, boardConfig):
        '''
        Constructor to initialize board array
        '''
        self.boardConfig=boardConfig
     
    #Return Length of board array
    def Length(self):
        return len(self.boardConfig)
        
    #Return size of puzzle (N)
    def CalN(self):
        return int(math.sqrt(self.Length()))
    
    #Printing current sate of board
    def PrintBoard(self):
        temp=1
        N=self.CalN()
        for i in self.boardConfig:
            print i,
            if temp==N:
                print
                temp=1
            else:
                temp=temp+1

    #Return goal Board Configuration             
    def GoalBoard(self):
        goal=list(self.boardConfig)
        goal.sort()
        return goal
    
    def MoveUp(self):
        N = self.CalN()
        loc = self.boardConfig.index(0)
        newBoardConfig = list(self.boardConfig)
        if loc < N:
            return None
        else:
            swap(newBoardConfig,loc-N,loc)
            return newBoardConfig
        
    def MoveDown(self):
        N = self.CalN()
        loc = self.boardConfig.index(0)
        newBoardConfig = list(self.boardConfig)
        if loc >=  self.Length()-N:
            return None
        else:
            swap(newBoardConfig,loc+N,loc)
            return newBoardConfig
    
    def MoveRight(self):
        N = self.CalN()
        loc = self.boardConfig.index(0)
        newBoardConfig = list(self.boardConfig)
        borderCase = list(range(N-1,N*N,N))
        if loc in borderCase :
            return None
        else:
            swap(newBoardConfig,loc+1,loc)
            return newBoardConfig
    
    def MoveLeft(self):
        N = self.CalN()
        loc = self.boardConfig.index(0)
        newBoardConfig = list(self.boardConfig)
        borderCase = list(range(0,N*N,N))
        if loc in borderCase :
            return None
        else:
            swap(newBoardConfig,loc-1,loc)
            return newBoardConfig
    
    