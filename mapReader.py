'''TO EDIT MAP, GOTO map.txt \n
map.txt format: \n
<edge name>,<'from' node name>,<'to' node name>,<total length>,<length ouside>,<crowdedness>,<visited?>,<directional>'''
from graph import Graph as grf
class mapReader:
   
    def __init__(self,fname):
        '''takes as input a text file path and parses it to produce a list of edges'''
        FILE = open(fname)
        temp = FILE.read().split('\n')
        self.EdgeList = []
        for e in temp:
            self.EdgeList.append(e.split(','))


    def makeGraph(self):
        '''uses the list of edges generated to produce a graph object'''
        graph = grf()
        counter = 0
        for e in self.EdgeList:
            graph.Edges.append(grf.Edge(e[1],e[2],e[-1],{"id":e[0],"totalLength":e[3],"outsideLength":e[4],"crowdPotential":e[5],"visited":e[6]}))

            for i in [1,2]:
                if e[i] not in graph.Nodes:
                    s = set()
                    s.add(counter)
                    graph.Nodes[e[i]] = grf.Node(0,s)
                else:
                    graph.Nodes[e[i]].Edges.add(counter)
            counter += 1
        return graph
        
        

# mp = mapReader('map.txt')
# #print(mp.EdgeList)
# graph = mp.makeGraph()
# #print([(o.values.get("id"), (o.endpoints.get("from"), o.endpoints.get("to"))) for o in graph.Edges])
# print([i for i in graph.Nodes.keys()])
# print('-'*100)
# print([i.Edges for i in graph.Nodes.values()])
