'''
Created on Jan 29, 2017

@author: saumitra
'''
def swap(boardConfig,loc1,loc2):
    temp=boardConfig[loc1]
    boardConfig[loc1]=boardConfig[loc2]
    boardConfig[loc2]=temp
    return boardConfig
