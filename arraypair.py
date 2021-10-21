# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Given array A, Can the array be split into pairs that are of equal value. For example, A = [1, 2, 1, 2]
# would have sub array pairs [1, 1] and [2, 2] 

A = [1, 2, 3, 4]
A2 = [1, 1]
A3 = [1, 2, 3, 4, 4, 3, 2, 1]
A4 = [1, 2, 3, 4, 1, 2, 3]
A5 = [2, 2]
A6 = [2, 3, 4, 2, 4, 3]

def solution(A):
    # write your code in Python 3.6
    j = 1
    length = len(A)

    #Edge case if list is odd

    if len(A)%2 != 0:

        return False

    for number1 in A:
        match = False
        while(j < length and not match):
            if(number1 == A[j]):
                match = True
            j+=1
        if (not match):
            return False
        else:
            return True


print(solution(A))
print(solution(A2))
print(solution(A3))
print(solution(A4))
print(solution(A5))
print(solution(A6))