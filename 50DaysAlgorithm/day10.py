def solution(a,b):
    a.sort()
    b.sort(reverse=True)
    answer = []
    for a,b in zip(a,b):
        answer.append(a*b)
    return answer
