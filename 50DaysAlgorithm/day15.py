#배열을 오름차순 정렬, 리턴 값은 배열의 인덱스 값으로
def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(i)

    answer.sort(key=lambda x: arr[x])

    return answer