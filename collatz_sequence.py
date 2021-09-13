
class collatzNumbers:

    def main():
        n = 100
        n2 = n
        collatzLength = 0
        longestCollatzLength = 0

        while(n2 > 1):
            n = n2
            print("Starting with n = " + str(n))

            while (n >= 1):
                collatzLength += 1
                print(n)
                if (n==1):
                    print("You have reached n  = " + str(n))
                    break
                elif (n%2 == 0):
                    n = n/2
                else:
                    n = 3*n+1

            print("Collatz length = " + str(collatzLength))
            if(collatzLength > longestCollatzLength):
                longestCollatzLength = collatzLength
            collatzLength = 0
            n2 -= 1
        print("Longest Collatz length was " + str(longestCollatzLength))
    if __name__ == "__main__":
        main() 