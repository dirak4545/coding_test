#정수 배열을 오름차순으로 정렬
def solution(arr):
    arr.sort()
    return arr
#-> sort는 원본 배열 자체를 바꾼다. 만약 리스트를 그대로 두고 출력만 정렬 한다면?

def solution2(arr):
    sorted_arr = sorted(arr)
    return sorted_arr

#버블 정렬
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
