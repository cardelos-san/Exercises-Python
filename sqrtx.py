## Calcuates the square root of a positive integer without using built-in functions

## Only works with whole numbers as expotents

""" 
:param  int a = base
:param  int b = exponent

"""
def power(a,b):
    nthPow = 1
    if (b==0):
        return 1
    while 0<b:
        nthPow = nthPow * a
        b -= 1
    return nthPow


if __name__ == "__main__":
    print(power(2,5))