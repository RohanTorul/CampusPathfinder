from graph import Graph as gr
from PriorityQueue import PrioQ as pq

class pathfinder:
    '''Class responsible for all pathfinding algorithms'''
    def __init__(self,graph,weightfunctions):
        self.graph:gr = graph
        self.weightfunctions = weightfunctions
        self.heuristic = lambda x:0
        '''Dummy function, does nothing atm'''
        self.infinity = float('inf')
    
    def _resetweights(self,start):
        '''Initialise the weight/cost of nodes'''
        for k in self.graph.Nodes.keys():
            if k != start:
                n = self.graph.getNode(k)
                n.value = self.infinity
            else:
                n = self.graph.getNode(k)
                n.value = 0
    
    def _resetvisited(self):
        '''sets all routes as not visited'''
        for e in self.graph.Edges:
            e.values['visited'] = 0
    
    def _reset(self,start,routeJournal:dict):
        '''calls _resetweights,_resetvisited, and clears the routeJournal'''
        self._resetweights(start)
        self._resetvisited()
        routeJournal.clear()
        for k in self.graph.Nodes.keys():
#                                     [cost, connected node, Edge reference]            
            routeJournal.setdefault(k,[self.infinity,'UNKNOWN','UNKNOWN']) if k != start else routeJournal.setdefault(k,[0, k,'start'])

    def _calculateCost(self,current,path,wf,time):
        return self.graph.getNode(current).value + self.weightfunctions[wf](path,time) + self.heuristic(path)
    
    def updateJournal(self,routeJournal:dict,NodeProbingQueue:pq,f,t):
        '''update the route information in the journal to reflect new data upon going through a new route.'''
        nodename = NodeProbingQueue.Dequeue()
        if nodename != None:
            connectingEdges = self.graph.getNode(nodename).Edges
            for e in connectingEdges :
                edge = self.graph.Edges[e]
                if edge.values['visited'] == 0 and not (edge.directional == 1 and edge.endpoints['to']  == nodename) :
                    ConnectingNode = edge.otherEnd(nodename)
                    edgeName = edge.values['id']
                    # print("checking: ",nodename,ConnectingNode,' via ',edgeName)
                    cost = self._calculateCost(nodename,self.graph.Edges[e],f,t)
                    self.graph.getNode(ConnectingNode).value = cost
                    NodeProbingQueue.Enqueue(ConnectingNode,cost)
                    if cost < routeJournal[ConnectingNode][0]:
                        routeJournal[ConnectingNode] = [cost,nodename, edgeName]
                    edge.values['visited'] = 1
                
    def parseJournal(self,routeJournal,start,end):
        '''reads the journal and summarises it into a list of connected nodes from start to destination'''
        prober = end
        route = []
        while prober != start:
            #print(routeJournal[prober][2])
            path = routeJournal[prober][2]
            route.insert(0,(prober,path))
            prober = routeJournal[prober][1]
        path = routeJournal[prober][2]
        route.insert(0,(prober,path))
            
        return route
        


    def A_star(self,start, end, weightfunction,time):
        '''The function to call to initiate pathfinfing algorithm'''
        NodeProbingQueue = pq()
        '''
        Minimum Priority queue storing recently visited paths in ascending cost
        Analogous to Prober's compass in the pdf document
        '''
        NodeProbingQueue.maxKey = self.infinity
        routeJournal = {}
        '''
        dictionary storing information on the current shortest paths.
        {key: Name of node, Value: [cost of shortest path, previous immediate node along that path, reference to the Edge connecting this node to the previous node]}
        Analogous to Prober's journal in the pdf document
        '''
        self._reset(start,routeJournal)
        '''begins by resetting the graph weights and visited'''
        NodeProbingQueue.Enqueue(start,0)
        while(len(NodeProbingQueue.priorityQueue) != 0):
            '''while the probing Queue(compass) is pointing at a node, go to the node and update the journal if needed'''
            self.updateJournal(routeJournal,NodeProbingQueue,weightfunction,time)

        return self.parseJournal(routeJournal,start,end)

