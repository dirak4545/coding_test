numbers = list(map(int, input()))
answer = 0

for i in numbers:
    # if i == 0 or i == 1:
    #     answer += i
    # else :
    #     if answer == 0:
    #         answer = 1
    #     answer *= i
    if i <= 1 or answer <= 1:
        answer += i
    else:
        answer *= i

print(answer)

#1 0 5 케이스 6이 나올 수 있게
#answer 가 1인 경우에는 곱하는 것보다 더하는 것이 이득
