n = int(input())
storage = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

storage.sort()

def binary_search(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in range(m):
    print(binary_search(storage, request[i], 0, n-1))