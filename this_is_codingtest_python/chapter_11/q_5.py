n, m = map(int, input().split())
balls = list(map(int, input().split()))
answer = 0
weights = [0] * 11 # 각 인덱스가 무게, 별로 몇 개의 공이 있는지

#무식하게
# for i in range(n):
#     for j in range(i+1, n):
#         if balls[i] == balls[j]:
#             continue
#         else:
#             answer += 1

#우아하게
#공 무게 별로 인덱스를 저장
for ball in balls:
    weights[ball] += 1

for i in range(1, m+1):
    n -= weights[i]
    answer += weights[i] * n

print(answer)