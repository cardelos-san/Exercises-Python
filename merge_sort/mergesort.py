## Recursive method
def mSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]

        mSort(leftArr)
        mSort(rightArr)
        merge(arr, leftArr, rightArr)
    return arr

## Merging
def merge(arr, leftArr, rightArr):
    i = 0
    j = 0
    k = 0

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i+=1
        else:
            arr[k] = rightArr[j]
            j+=1
        k+=1

    while i < len(leftArr):
        arr[k] = leftArr[i]
        i+=1
        k+=1
        
    while j < len(rightArr):
        arr[k] = rightArr[j]
        j+=1
        k+=1

if __name__ == '__main__':
    pass