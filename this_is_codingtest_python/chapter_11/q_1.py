n = int(input())
traveler = list(map(int, input().split()))
answer = 0

# --- 1차 시도: 공포도가 큰 사람부터 처리하며 동료를 끌어모으는 방식 ---
# 경계값(tmp vs len(traveler)) off-by-one은 고쳤었지만, 그걸로도 부족했음.
# 반례: [1, 1, 3] -> 정답은 2(그룹 {1}, {1} 두 개)인데, 이 방식은 3을 먼저
# 처리하면서 1,1을 둘 다 끌어다 써버려서 그룹 {3,1,1} 1개만 만들어짐.
# "공포도 큰 사람부터 만족시키기"는 작은 공포도 사람들을 낭비시켜서
# 그룹 개수가 오히려 줄어듦 -> 처리 순서 자체가 틀린 전략이었음.
#
# traveler.sort(reverse=False)
# while traveler:
#     tmp = traveler.pop()
#     if tmp - 1 > len(traveler):
#         break
#     if tmp - 1 == len(traveler):
#         for i in range(tmp - 1):
#             traveler.pop()
#         answer += 1
#         break
#     for i in range(tmp-1):
#         traveler.pop()
#     answer += 1

# --- 2차: 공포도가 작은 사람부터 처리 (동료를 "모으다가" 채워지면 그룹 확정) ---
# sort(reverse=True) + pop()을 쓰면 여전히 pop() 한 번으로 O(1)에
# "가장 작은 값부터" 꺼낼 수 있음 (내림차순 리스트의 맨 끝이 최솟값이라서).
traveler.sort(reverse=True)

count = 0
while traveler:
    fear = traveler.pop()   # 가장 작은 공포도부터 꺼냄
    count += 1               # 지금 모인 동료 수(자기 자신 포함)
    if count >= fear:        # 이 사람 기준으로 그룹이 완성됨
        answer += 1
        count = 0

print(answer)
