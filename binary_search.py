## This module utilizes merge sort if array is unsorted, then uses binary search to find target in array

from mergesort import mSort

def bSearch(nums, target):

    ## Sort if not sorted
    if(not isSorted(nums)):
        print("Array not sorted, sorting")
        mSort(nums)
    
    ## Searching
    lower = 0
    upper = len(nums)-1
    found = False
    
    ## Main Loop
    while(lower <= upper):
        mid = (lower + upper)//2
        if(nums[mid] == target):
            found = True
            break
        elif(nums[mid] < target):
            lower = mid + 1
        elif(nums[mid] > target):
            upper = mid - 1
    
    if(found):
        print("Target", target, "found at position", mid)
    else:
        print("Target not found in array")

    print( nums )

## Checks if array is sorted
def isSorted(arr):
    flag = False

    if(all(arr[i] <= arr[i+1] for i in range(len(arr)-1))):
        flag = True

    return flag

test = [1,2,3,5,8,9,4,20,30,10]

if __name__ == "__main__":
    print("Using Binary Search on Array:", test)
    bSearch(test, 0)