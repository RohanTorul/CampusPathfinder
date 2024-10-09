class Graph:
    '''custom Graph data type '''
    class Node:
        'stores a value(s) and a set of references to edges(int) it is connected to'
        def __init__(self):
            self.value = None
            self.Edges = set()
            # self.searchfunction = lambda x: x.value
        def __init__(self,val,edges):
            self.value = val
            self.Edges = edges
            # self.searchfunction = lambda x: x.value
    class Edge:
        '''Stores user defined values(dictionary),whether it is uni or bi-directional and reference to nodes at each end(String)'''
        def __init__(self,n1,n2,directional = False, values = {}):
            self.values:dict = values
            self.directional = directional
            self.endpoints = {'from':n1,'to':n2}
            self.otherEnd = lambda x: self.endpoints['to'] if x == self.endpoints['from'] else self.endpoints['from'] 

    def __init__(self):
        self.Nodes:dict[str:self.Node] = dict()
        '''Dictionary mapping node references(String) to node objects'''
        self.Edges:list[self.Edge] = list()
        '''list of all the edges in the Graph'''
        self.getNode = lambda name: self.Nodes.get(name)
        '''Returns Node object corresponding to it's reference(String)'''
        
        

        