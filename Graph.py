'''
Michael Wilson
A simple graph class.

A Graph is a data structure which is a collection of vertices linked by edges.
In the case of this graph class, we will represent the contents of it by an 
adjaceny list style. The reason for this is that the graph will not ve very dense.
'''

from . import Edge.py
from . import Vertex.py
from . import LinkedList.py

class Graph:

    '''
    Constructor 
    RT: O(VE)

    param vertices --> The list of vertices for the graph.
    param edges --> The set of edges associated in this graph.
    '''
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjList = []

        # iterate through the vertices and create the list
        # RT: O(V)
        for vertex in Vertices:
            
            # iterate through the edges and add the appropriate mappings
            # RT: O(E)
            for edge in edges:
                if edge.source == vertex:
                    vertex.add(edge.destination, edge.cost, None)

            self.adjList.append(vertex)
                    

