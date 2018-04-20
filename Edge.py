'''
Michael Wilson 
Simple edge class.

An edge is nothing more than a connection between two vertices which may or 
may not have some sort of cost associated with it.
'''

from . import Vertex.py

class Edge:

    '''
    Constructor

    param cost --> The cost associated with this edge.
    param source --> The source vertex.
    param destination --> The destination vertex.
    '''
    def __init__(self, cost, source, destination):
        self.cost = cost
        self.source = source
        self.destination = destination