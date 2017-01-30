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
        Constructor to initialize board Configuration and Board Size(N)
        '''
        #Keeping boardConfig as tuple for faster search
        self.boardConfig=tuple(boardConfig)
        #Size of the board
        self.N=int(math.sqrt(len(self.boardConfig)))
    
    #Printing current sate of board
    def PrintBoard(self):
        temp=1
        for i in self.boardConfig:
            print i,
            if temp==self.N:
                print
                temp=1
            else:
                temp=temp+1

    #Return goal Board Configuration             
    def GoalBoard(self):
        goal=list(self.boardConfig)
        goal.sort()
        return tuple(goal)
    
    #Return Board Configuration by moving one space Up else None
    def MoveUp(self):
        N = self.N
        loc = self.boardConfig.index(0)
        newBoardConfig = list(self.boardConfig)
        #Location of 0 should be not be less than index for top row for possible UP movement
        if loc < N:
            return None
        else:
            swap(newBoardConfig,loc-N,loc)
            return newBoardConfig
        
    #Return Board Configuration by moving one space Down else None        
    def MoveDown(self):
        N = self.N
        loc = self.boardConfig.index(0)
        newBoardConfig = list(self.boardConfig)
        #Location of 0 should be greater than or equal to index of last row for possible DOWN movement
        if loc >=  len(self.boardConfig)-N:
            return None
        else:
            swap(newBoardConfig,loc+N,loc)
            return newBoardConfig

    #Return Board Configuration by moving one space Right else None    
    def MoveRight(self):
        N = self.N
        loc = self.boardConfig.index(0)
        newBoardConfig = list(self.boardConfig)
        #Set to capture Right Most index in each row of table 
        borderCase = set(range(N-1,N*N,N))
        #Location of 0 should not in equal to any of Right Most index of each row of table
        if loc in borderCase :
            return None
        else:
            swap(newBoardConfig,loc+1,loc)
            return newBoardConfig

    #Return Board Configuration by moving one space Left else None    
    def MoveLeft(self):
        N = self.N
        loc = self.boardConfig.index(0)
        newBoardConfig = list(self.boardConfig)
        #Set to capture Left Most index in each row of table 
        borderCase = set(range(0,N*N,N))
        #Location of 0 should not in equal to any of Left Most index of each row of table
        if loc in borderCase :
            return None
        else:
            swap(newBoardConfig,loc-1,loc)
            return newBoardConfig