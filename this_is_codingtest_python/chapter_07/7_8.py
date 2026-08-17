# --- 기존 코드 (배열에서 값 m의 인덱스를 찾는 코드였음. 떡볶이 떡 만들기 문제와는 다른 문제) ---
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)
#
# n, m = map(int, input().split())
# array = list(map(int, input().split()))
# result = binary_search(array, m, 0, max(array))
# result = binary_search(array, m, 0, n-1)
#
# print(result)

# --- 떡볶이 떡 만들기 (파라메트릭 서치) ---
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
