from slinkedlist import SLList

def run():
    a = SLList()

    a.insert("I'm a node!")

    a.insert("I'm another node!")

    a.displayListSize()

    a.printAll()

    a.insert("Yet another node...")

    a.insert("ok last node")

    a.printAll()

    a.displayListSize()


    


if __name__ == "__main__":
    run()