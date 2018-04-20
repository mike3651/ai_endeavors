'''
Michael Wilson
A simple graph class.

A Graph is a data structure which is a collection of vertices linked by edges.
In the case of this graph class, we will represent the contents of it by an 
adjaceny list style. The reason for this is that the graph will not ve very dense.
'''

from . import Edge.py

class Graph:

    '''
    Constructor 

    param vertices --> The list of vertices for the graph.
    param edges --> The set of edges associated in this graph.
    '''
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges