## This module calcultes the nth Fibonacci term using iteration and recursion

class Fibonacci:

    # Recursive method
    def rFibonacci(self, n):

        rf = Fibonacci()
        
        if n == 0:
            return 0
        
        elif n == 1 or n == 2:
            return 1
        
        else:
            return rf.rFibonacci(n - 2) + rf.rFibonacci(n - 1)
        

    # Iterative method
    def iFibonacci(self, n):

        if n == 0:
            return 0

        elif n == 1 or n == 2:
            return 1


        sum = 0
        n1 = 0
        n2 = 1

        for i in range(0, n - 1):
            sum = n1 + n2
            n1 = n2
            n2 = sum
        return sum
            
            
        

if __name__ == "__main__":

    f = Fibonacci()
    n = 10
    print("Calculating the nth Fibonacci term using iteration: ")
    print("n = ", n)
    print(f.iFibonacci(10))
    print("Calculating 0 to nth Fibonacci terms using iteration: ")
    for i in range(n + 1):
        print(f.iFibonacci(i))
    
    n = 20

    print("Calculating the nth Fibonacci term using recursion: ")
    print("n = ", n)
    print(f.rFibonacci(n))
    print("Calculating 0 to nth Fibonacci terms using iteration: ")
    for i in range (n + 1):
        print(f.rFibonacci(i))

    