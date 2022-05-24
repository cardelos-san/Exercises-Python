
# Given an array, and a target, find a sum of two elements in array such that sum = target
# Time Complexity  O(n^2)
# Space Complexity O(1)


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]

    """
    sum = 0
    result = []
    for i, num in enumerate(nums):
        j = i + 1
        while (j < len(nums)):
            sum = num + nums [j]
            if(sum == target):
                result.append(i)
                result.append(j)
                return result
            j+=1
    

if __name__ == "__main__":
    inputNums = [2, 5, 5, 11]
    inputTarget = 13

    print(twoSum(inputNums, inputTarget))
