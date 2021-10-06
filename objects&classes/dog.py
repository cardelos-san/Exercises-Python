
## Dog class inherits from parent class Animal 

from animal import Animal

class Dog(Animal):

    """
    :override parent method
    """
    def makeSound(self):
        print("Woof! Woof!")