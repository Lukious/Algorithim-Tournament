#백준6603

def re_lotto(n,T):
    global range_arr
    for i in range_arr[n]:
        if i in T:
            continue
        else:
            if T[n-1] > i:
                continue
            if n < 5 :
                T[n] = i
                re_lotto(n+1,T)
                T[n + 1] = 0
            else:
                print(' '.join(map(str, T[:-1])),end=' ')
                print(i)


def lotto():
    global range_arr
    for i in range_arr[0]:
        T = [0,0,0,0,0,0]
        T[0] = i
        re_lotto(1,T)
