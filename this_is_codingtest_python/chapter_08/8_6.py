n = int(input())
array = list(map(int, input().split()))

d = [0] * 100
answer = 0

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

answer = d[n-1]

print(answer)

#i번째 창고를 턴 다고 생각해보자
#i번째 창고를 털면 지금까지 턴 값 d[i-2] 그리고 i번째
#창고값 d[i] = d[i-2] + array[i] vs d[i-1]