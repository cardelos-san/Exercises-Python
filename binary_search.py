from merge_sort import mSort

def bSearch(nums, target):

    ## Sort if not sorted
    if(not isSorted(nums)):
        print("Array not sorted, sorting")
        mSort(nums)
    
    ## Searching
    lower = 0
    upper = len(nums)-1
    found = False
    
    ## Infinite Loop if target not in array. Needs debugging
    while(not found):
        mid = (lower + upper)//2
        if(nums[mid] == target):
            found = True
        elif(nums[mid] < target):
            lower = mid
        elif(nums[mid] > target):
            upper = mid
        elif(upper == 2):
            print("Target not in array")
            break
    
    if(found):
        print("Target", target, "found at position", mid)

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