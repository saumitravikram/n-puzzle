'''
Created on Jan 29, 2017

@author: saumitra
'''


def swap(boardConfig,loc1,loc2):
    temp=boardConfig[loc1]
    boardConfig[loc1]=boardConfig[loc2]
    boardConfig[loc2]=temp
    return boardConfig

'''
boardConfig <tuple>
fringeBoard <set>
exploredBoard <set> 
'''
def compareState(boardConfig,fringeBoard,exploredBoard):
    if boardConfig in fringeBoard or boardConfig in exploredBoard:
        return True
    else:
        return False
