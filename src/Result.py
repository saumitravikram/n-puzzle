'''
Created on Jan 29, 2017

@author: saumitra
'''

class Result():
    '''
    classdocs
    '''

    def __init__(self,State,explored,fringe,max_fringe_size,max_search_depth):
        '''
        Constructor to initialize Result class
            goalState
            list of explored state
            list of state in fringe node when goal found
            maximum size of fringe at a given time
            maximum size of search tree
        '''
        self.dect={}
        self.state=State
        self.explored=explored
        self.fringe=fringe
        self.dect['path_to_goal']=[]
        self.dect['cost_to_path']=0
        self.dect['nodes_expanded']=0
        self.dect['fringe_size']=0
        self.dect['max_fringe_size']=max_fringe_size
        self.dect['search_depth']=0
        self.dect['max_search_depth']=max_search_depth;
     
    #Wrapper function to call all other function to generate all attributes of results   
    def computeResult(self):
        self.pathToGoal()
        self.nodeExpanded()
        self.fringeSize()
        self.searchDepth()
    
    #Returns list of moves taken to reach Goal state from root state
    def pathToGoal(self):
        temp = self.state
        while temp.parent != None :
            self.dect['path_to_goal'].append(temp.move)
            self.dect['cost_to_path']+=1
            temp = temp.parent
        self.dect['path_to_goal'].reverse()
        
    #return nodes expanded in search tree
    def nodeExpanded(self):
        self.dect['nodes_expanded']=len(self.explored)-1
    
    #Return the number of nodes in fringe
    def fringeSize(self):
        self.dect['fringe_size']=len(self.fringe)
        
    #Return the depth of Goal State from root state    
    def searchDepth(self):
        self.dect['search_depth']=self.state.cost