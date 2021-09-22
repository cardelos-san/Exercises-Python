##Example implementation of 2D array
zeros =[ [0]*10 for _ in range(5)]

##2D array implementation using simplied Python notation
zerosTwo = [[0 for columns in range(10)] for rows in range(5)]

##Replace the very last value of the matrix
zeros[-1][-1] = 20

##Replace value at row 0, column 3
zerosTwo[0][3] = 10

##Printing
print(zeros)

##Dictionary implementation which contains Variable name as key, and a 2D array as value
dict = {
    "Variable_Name": "zeros",
    "Data": zeros
}

##Printing
print("Printing first array: ")
for rows in zerosTwo:
    print(rows)

print("Printing second array with Variable Name:", dict["Variable_Name"])
for rows in dict["Data"]:
    print(rows)
