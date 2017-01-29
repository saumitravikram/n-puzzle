'''
Created on Jan 29, 2017

@author: saumitra
'''
import sys
from State import State

#Function to read user input arguments
def readArgs():
    global searchAlgo
    global boardConfig
    searchAlgo=sys.argv[1].upper()
    boardConfig=map(int,(sys.argv[2].split(',')))

if __name__ == '__main__':
    
    #Read the input arguments to create board and search logic to use
    readArgs()
    
    state=State(None,boardConfig,None)
    state.PrintBoard()
    state.isGoal()
    if state.isGoal():
        print 'T'
    else:
        print 'F'
    newList=[]
    newList=state.neighbour()
    for childState in newList:
        childState.PrintBoard()
        print