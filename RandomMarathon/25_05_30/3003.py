#킹1, 퀸1, 룩2, 비숍2, 나이트2, 폰8
n = (list(map(int, input().split())))

answer = [ 1, 1, 2, 2, 2, 8 ]

for i in range(6):
    answer[i] -= n[i]
    print(answer[i])
