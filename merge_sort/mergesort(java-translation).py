
# This was a Java implementation of merge sort that I had done earlier and tried to translate
# It does not work as intended and needs debugging

class MergeSort:
    
    ##Constructor
    def __init__(self, arrayToSort):
        self.arrayToSort = arrayToSort
        self.unsortedCopy = arrayToSort
        self.left = 0
        self.right = len(self.arrayToSort)-1

    ##Initial Merge Sort call
    def sort(self):
        self.mergeSort(self.left, self.right)

    ##Merge Sort 
    def mergeSort(self, left, right):
        if(left < right):
            mid = (left + right)/2
            self.mergeSort(left, mid)
            self.mergeSort(mid+1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        nLeft = mid - left + 1
        nRight = right - mid

        leftArr = self.arrayToSort[left : mid+1]  # Needs debbuging (Python array slicing)(Maybe check the starting and end points(?))
        rightArr = self.arrayToSort[mid+1 : right+1] # Needs debbuging (Python array slicing)

        i = 0
        j = 0
        k = left

        while(i < nLeft and j < nRight):
            if(leftArr[i] <= rightArr[j]):
                self.arrayToSort[k] = leftArr[i]
                i+=1
            else:
                self.arrayToSort[k] = rightArr[j]
                j+=1
            k+=1
        
        while(i < nLeft):
            self.arrayToSort[k] = leftArr[i]
            i+=1
            k+=1

        while(j < nRight):
            self.arrayToSort[k] = rightArr[j]
            j+=1
            k+=1

