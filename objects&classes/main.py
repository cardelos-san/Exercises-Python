## Polymorphism & inheritance exercise

from dog import Dog
from cat import Cat

def run():

    dogList = []
    catList = []

    newDog = Dog("Dog", "Brown", "Max", "Josh")

    dogList.append(newDog)

    newCat = Cat("Cat", "White", "Felix", "Ramon")

    catList.append(newCat)

    newCat.setNewOwner("Toby")
    
    print(newCat.toDisplay())

    print(displayPrompt())

    kbd = input('')

    while(not kbd == 'q'):

        if kbd == 'a':
            print("Creating new Dog object ")
            type = "Dog"
            name = input("Enter name: ")
            color = input("Enter color: ")
            owner = input("Enter owner name: ")

            newDog = Dog(type, color, name, owner)

            print("\nEntry created succesfully, storing in list\n")

            dogList.append(newDog)


        elif kbd == 'b':
            print("Creating new Cat object ")
            type = "Cat"
            name = input("Enter name: ")
            color = input("Enter color: ")
            owner = input("Enter owner name: ")

            newCat = Cat(type, color, name, owner)

            print("Entry created succesfully, storing in list")

            catList.append(newCat)
        
        elif kbd == 'c':
            print("Displaying all Dog entries:\n")
            for dog in dogList:
                print(dog.toDisplay()) 
                
        elif kbd == 'd':
            print("Displaying all Cat entries:\n")
            for cat in catList:
                print(cat.toDisplay())

        else:
            print("Invalid input")

        print(displayPrompt())
        kbd = input('')


def displayPrompt():
    prompt = "Make a selection:\n\n" \
    + "a) Create Dog object\n" \
    + "b) Create Cat object\n" \
    + "c) Display Dog list\n" \
    + "d) Display Cat list\n" \
    + "Enter q to Quit anytime" \

    return prompt

if __name__ == "__main__":
    run()