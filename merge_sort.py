class MergeSort:
    def setup(array):
        left = 0
        right = len(array)-1
    
    def sort(left, right):
        if(left < right):
            mid = (left + right)/2
            sort(left, mid)
