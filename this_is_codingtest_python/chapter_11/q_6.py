# def solution(food_times, k):
#     answer = 0
#     time = 0
#     # table_num = time % len(food_times)
#     # for i in range(1, k+1):
#     #     table_num = (i - 1) % len(food_times)
#     #     if food_times[table_num] == 0:
#     #         continue
#     #     else:
#     #         food_times[table_num] -= 1
#     while k:
#         table_num = (time) % len(food_times)
#
#         if food_times[table_num] == 0:
#             time += 1
#             continue
#         else:
#             food_times[table_num] -= 1
#             k -= 1
#
#     answer = table_num - 1
#
#     return answer
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1          # 음식 하나가 없어졌으니 한 바퀴 도는 인원(길이)도 줄여야 함
        previous = now

    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]