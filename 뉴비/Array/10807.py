l = int(input())
m = list(map(int, input().split()))
n = int(input())
answer = 0

for i in m:
    if i == n:
        answer += 1

print(answer)