class Node:

    ## New node constructor 
    def __init__(self, element):
        self.element = element
        self.nextElement = None
    
    ##  Returns current node
    def getElement(self):
        return self.element

    ## Returns next node
    def getNext(self):
        return self.nextElement
    
    ## Sets next node
    def setNext(self, element):
        self.nextElement = element