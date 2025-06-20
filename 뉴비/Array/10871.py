n = map(int, input().split())
n = list(n)
m = map(int, input().split())
m = list(m)
answer = ''

for i in m:
    if i < n[1]:
        answer += str(i) + ' '

print(answer)