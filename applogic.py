'''
THIS FILE CONTAINS FUNCTIONS USED IN GUI.PY
TO EDIT MAP, GOTO map.txt\n
map.txt format: \n
<edge name>,<'from' node name>,<'to' node name>,<total length>,<length ouside>,<crowdedness>,<visited?>,<directional>
'''

from PathFinder import pathfinder as pf
from graph import Graph as grf
from mapReader import mapReader as mr
import math as m


# Step function
u = lambda t: 0 if t < 0 else 1

# P1(x)
#P1 = lambda x: (m.exp((x / 12) * m.log(11)) - 1) * u(x - 7.5)
r=1.3;o=1;s=0.1
P1 = lambda x,: 10 / (1 + m.exp(-r * (x - o * 9.75))) + s

# P2(x)
k = 10
P2 = lambda x: (-1 * (m.exp(-1 * ((k * u(k) + 2) * (x - 12+0.001) ** -2))) + 1) * 10 * u(x - 12)

# P(x) crowdedness coefficient
P = lambda x: (P1(x) if x < 12 else (P2(x) if x < 19 else 0))*1/10



def weightfunction0(edge:grf.Edge,t=0):
    '''Weight Function for shortest path'''
    return int(edge.values['totalLength'])
def weightfunction1(edge:grf.Edge,t=0):
    '''Weight Function for shortest outdoors path'''
    return int(edge.values['outsideLength']) #+ int(edge.values['totalLength'])

def weightfunction2(edge:grf.Edge, Time):
    '''Weight Function for least crowded path'''
    # v=  P(Time)
    # print(Time,v)
    return  P(Time)* float(edge.values['crowdPotential'])*int(edge.values['totalLength']) + int(P(Time) < 0.1) *int(edge.values['totalLength']) #+ int(edge.values['totalLength'])


algos = {"Shortest way":0, "least outdoors":1, "least crowded":2}
'''maps text input (from GUI) to list index '''
def GetPathDescription(a):
    '''Gets a list as result from Pathfinder and returns directions in a sentence'''
    pathStr = f"Start at {a[0][0]}, then go to "
    for p in a[1:-1]:
        pathStr = pathStr + (f"{p[0]} via {p[1]} then go to ")
    pathStr = pathStr + (f"{a[-1][0]} via {a[-1][1]} and you will reach your destination")
    return pathStr

mapreader = mr('map.txt')
'''MapReader Object to turn text file representation of a graph into a graph object'''
Graph = mapreader.makeGraph()
'''Graph object as modelled by Map.txt'''
pathfinder = pf(Graph,[weightfunction0,weightfunction1,weightfunction2])
'''Pathfinder object encapsulating all of the Pathfinding logic'''
PathFound = lambda start, finish, algo, time : GetPathDescription(pathfinder.A_star(start,finish,algos[algo], time))
'''Lambda function compacting all of the inputing points, calculating path and processing an output string into one'''

#uncommnet this and change parameters as you wish and run to use CL instead of GUI
# NOT MEANT TO THOUGH....NO INPUT VALIDATION GUARANTEED. Validation is done at the GUI level.
#print(pathfinder.A_star('Engineering Building','Education Building',2))