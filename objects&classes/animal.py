class Animal(object):
    
    def __init__(self, type, color, name, originalOwner):
        self.type = type
        self.color = color
        self.name = name
        self.owner = originalOwner

    def setNewOwner(self, ownerName):
        self.owner = ownerName
        print("New owner name set to ", self.owner)
    
    ## Abstract method
    def makeSound(self):
        pass
    
    ## Returns a display of object attributes using dictionary
    def toDisplay(self): # -> dict[key, value]
        Attr = { 
            "Name": self.name,
            "Type": self.type,
            "Color": self.color,
            "Owner": self.owner
        }

        display = ''

        for attr in Attr:
            display = display + attr + " -> " + Attr[attr] + "\n"

        return display