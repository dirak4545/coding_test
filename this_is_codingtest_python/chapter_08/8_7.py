#타일을 채우는 경우의 수 1 X 2, 2 X 1, 2 X 2
n = int(input())
answer = 0

d = [0] * 100

d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = ()