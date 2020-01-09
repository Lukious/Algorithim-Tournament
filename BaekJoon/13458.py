#13458

import sys
import math

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
result = len(arr)
rest = [i - b for i in arr if i - b > 0]
rest2 = [math.ceil(i / c) for i in rest]
result += sum(rest2)
print(result)