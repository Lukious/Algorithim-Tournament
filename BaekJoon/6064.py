def getYearNumber(m,n,x,y):
    while x <= m*n:
        if (x-y)%n == 0:
            return x
        x += m
    return -1

TT = int(input())
for _ in range(TT):
    m, n, x, y = map(int, input().split())
    print( getYearNumber(m,n,x,y) )