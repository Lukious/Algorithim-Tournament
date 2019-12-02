def min(x, y):
    return x if x <= y else y
 
x = int(input())
 
minimum_count = [ 0 for _ in range(x+1)]
 
index = 0
while(True):
    if index > x:
        break
 
    if index <= 1:
        minimum_count[index] = 0
    else:
        temp_min = x + 1
        if index % 3 == 0:
            temp_index = int(index/3)
            temp_min = min(temp_min, minimum_count[temp_index])
 
        if index % 2 == 0:
            temp_index = int(index/2)
            temp_min = min(temp_min, minimum_count[temp_index])
 
        temp_min = min(temp_min, minimum_count[index-1])
        minimum_count[index] = int(temp_min + 1)
    index = index + 1
 
print(minimum_count[x])