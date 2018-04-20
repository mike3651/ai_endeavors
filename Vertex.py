'''
Michael Wilson
Simple vertex class.

A vertex is an entity that stores information relating to some sort of cost or reward.
'''

import . from LinkedList

class Vertex:
    '''
    Constructor 

    param name --> The identifier of this node.
    '''
    def __init__(self, name):
        self.name = name
        self.neighbors = LinkedList()
