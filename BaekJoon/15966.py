n = input()
num_arr = map(int, raw_input().split())
long_arr = [1] * n
num_idx_map = {num_arr[0]: 0}
max_long = 1
 
for i in xrange(1, n):

    if num_arr[i] - 1 in num_idx_map:
        long_arr[i] = long_arr[num_idx_map[num_arr[i] - 1]] + 1        
    else:
        long_arr[i] = 1
        
    if long_arr[i] > max_long: 
        max_long = long_arr[i]
        
    num_idx_map[num_arr[i]] = i

