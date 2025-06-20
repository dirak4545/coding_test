#유리수 정렬
def solution(rational):

    rational.sort(key=func)
    answer = [[rational]]
    return answer

def func(num):
    r∑eturn num[0]/num[1]