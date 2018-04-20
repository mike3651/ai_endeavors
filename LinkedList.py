'''
Michael Wilson
A simple linkedlist class.

The idea of a linked list is that it is nothing more than a chain of nodes link to one 
another.
'''

class LinkedList:
    # Constructor
    def __init__(self):
        self.front = None 

    '''
    addNode
    Adds a node to the front of the list.

    param data --> The data of the new node to generate.
    '''
    def addNode(self, data):
        if self.front == None:
            self.front = Node(data)
        else:
            self.front = Node(data, self.front)

    '''
    removeNode
    This function removes a node from the front of the list.
    '''
    def removeNode(self):
        self.removeNodeAt(0)

    '''
    removeNodeAt
    This function removes a node from the list a particular index

    param index --> The index of the target node to remove 
    '''
    def removeNodeAt(self, index):
        # Handle the front case 
        if index == 0:
            self.front = self.front.next

        # Handle every other case
        else:
            currIndex = 0
            curr = self.front
            while curr != None and currIndex < index - 1:
                currIndex += 1
                curr = curr.next
            
            if currIndex == index - 1:
                curr.next = curr.next.next 
            else: 
                print "No Node at the given index"

    '''
    getSize
    Returns the size of the list 
    '''
    def getSize(self):
        curr = self.front
        size = 0
        while curr != None:
            size += 1
            curr = curr.next
        return size
    

class Node:
    '''
    Constructor 
    Creates a new instance of a node object.

    param data --> The data value of this node.
    param cost --> The cost associated with this node.
    param next --> The link to the next node in this chain
    '''
    def __init__(self, data, cost, next):
        self.data = data
        self.cost = cost
        self.next = next