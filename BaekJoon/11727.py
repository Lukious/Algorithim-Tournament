def squares(n):
    answer = 0
    n1 = 1
    n2 = 3
    
    for i in range(1, n+1):
        if i == 1:
            answer += 1
        elif i == 2:
            answer += 2
        else:
            answer = n1 * 2 + n2
            n1 = n2
            n2 = answer
    return answer

answer = squares(int(input()))
print(answer % 10007)