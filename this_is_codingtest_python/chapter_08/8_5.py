n = int(input())
answer = 0
# while n != 1:
#     if n % 5 == 0:
#         n //= 5
#         answer += 1
#     elif n % 3 == 0:
#         n //= 3
#         answer += 1
#     elif n % 2 == 0:
#         n //= 2
#         answer += 1
#     else:
#         n -= 1
#         answer += 1
#
# print(answer)
#그리디로는 최소 횟수를 구할 수 없다!!!

# --- 여기까지는 직접 짠 DP 시도. 버그 2개 있었음 ---
# 1) d[i] = d[i-1] - 1  ->  -1이 아니라 +1이어야 함 (연산을 한 번 더 쓰는 거니까)
# 2) elif로 5/3/2를 묶어서 하나만 체크함 -> i가 여러 수로 동시에 나눠질 때
#    (예: 30은 5,3,2 다 나눠짐) 실제로는 셋 다 비교해서 최솟값을 골라야 하는데
#    elif라서 5로 나눠지면 3,2는 아예 검사를 안 하게 됨
# d = [0] * 30001
# for i in range(2, n+1):
#     d[i] = d[i-1] - 1
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5] + 1)
#     elif i % 3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)
#     elif i % 2 == 0:
#         d[i] = min(d[i], d[i//2] + 1)
# print(d[n])

d = [0] * (n + 1)   # d[i] = i를 1로 만드는 데 필요한 최소 연산 횟수

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1          # 1을 빼는 경우 (항상 가능한 기본값)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[n])
