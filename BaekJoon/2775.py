from math import factorial
TT = int(input())
for t in range(TT):
    k = int(input())
    n = int(input())
    print( factorial(k+n) // factorial(k+1) // factorial(n-1) )