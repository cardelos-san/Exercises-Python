from node import Node

class SLList:

    ## Singly Linked List constructor
    def __init__(self):
        self.headElement = None
        self.currentSize = 0

    ## Inserting new element at the beginning of list                   
    def insert(self, value): # value -> any

        element = Node(value)             ## Creating new node obj
        element.setNext(self.headElement) ## Creating pointer to head element before
        self.headElement = element        ## Creating pointer to element after
        self.currentSize += 1             ## Increasing list size
        print("New element created")

    ## Displays list size
    def displayListSize(self):
        print("List Size: ", self.currentSize)

    ## Prints every element in list
    def printAll(self):
        elementToPrint = self.headElement
        while elementToPrint is not None:
            print(elementToPrint.getCurrent())
            elementToPrint = elementToPrint.getNext()