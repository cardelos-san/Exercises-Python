import mergesort as ms


def findMultiples(x, y, range):

    multiplesX = []
    multiplesY = []

    i = 1

    while (i <= range):

        ##Finding all multiples of x
        resultX = i*x
        if resultX < range:
            multiplesX.append(resultX)

        ##Finding all multiples of y
        resultY = i*y
        if resultY < range:
            multiplesY.append(resultY)

        ##Creating a single list
        completeList = multiplesX + multiplesY
        
        #Removing duplicates
        completeList = list(set(completeList))

        #Sorting
        ms.mSort(completeList)

        i +=1
    return completeList


def sumOf(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum
        
if __name__ == "__main__":
    print(findMultiples(3,5, 1000))
    print(sumOf(findMultiples(3,5, 1000)))
