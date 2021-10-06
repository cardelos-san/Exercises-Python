from node import Node

class SLList:

    ## Singly Linked List constructor
    def __init__(self):
        self.headElement = None
        self.currentSize = 0

    ## Inserting new element                    
    def insert(self, value): # value -> any

        element = Node(value)             ## Creating new node obj
        element.setNext(self.headElement) ## Creating pointer to head element before
        self.headElement = element        ## Creating pointer to element after
        self.currentSize += 1             ## Increasing list size
        print("New element created")




    





