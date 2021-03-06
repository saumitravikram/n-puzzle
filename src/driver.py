'''
Created on Jan 29, 2017

@author: saumitra
'''
import sys
from State import State
from BFS import BFS
from DFS import DFS
import resource
import timeit

#Function to read user input arguments
def readArgs():
    global searchAlgo
    global boardConfig
    searchAlgo=sys.argv[1].upper()
    boardConfig=map(int,(sys.argv[2].split(',')))
    
def triggerSearch():
    global start
    global stop
    global result
    search=None
    state=State(None,boardConfig,None,0)
    if searchAlgo == 'DFS' :
        search=DFS(state)
    elif searchAlgo == 'BFS' :
        search=BFS(state)

    if search!=None:
        start = timeit.default_timer()
        result=search.searchAlgo()
        stop = timeit.default_timer()
    else:
        result=None
    
def printResult(result):
    if result!=None:
        result.computeResult()
        print 'path_to_goal: ' + str(result.dect['path_to_goal'])
        print 'cost_to_path: ' + str(result.dect['cost_to_path'])
        print 'nodes_expanded: ' + str(result.dect['nodes_expanded'])
        print 'fringe_size: ' + str(result.dect['fringe_size'])
        print 'max_fringe_size: ' + str(result.dect['max_fringe_size'])
        print 'search_depth: ' + str(result.dect['search_depth'])
        print 'max_search_depth: ' + str(result.dect['max_search_depth'])
        print 'running_time: ' + str(stop-start)
        print 'max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024))
    else:
        print 'Wrong parameters'

if __name__ == '__main__':
    
    #Read the input arguments to create board and search logic to use
    readArgs()
    
    #Trigger Search depending on type
    triggerSearch()
    
    #Print Result
    printResult(result)