#아이디어 연속된 숫자들을 청크로 묶어서 1과 0으로 단순화
#0 과 1 중 숫자 적은 놈이 정답

# --- 기존 코드: numbers를 순회하면서 동시에 numbers.remove()로 지움 ---
# for문으로 리스트를 돌면서 그 리스트 자체를 지우면, 지운 만큼 뒤 원소들이
# 앞으로 당겨지는데 반복문 인덱스는 그거랑 상관없이 그냥 +1씩 되니까
# 원소를 건너뛰는 버그가 생김 (예: "001001" -> [0,1,0,1]이 나와야 하는데 [0,1]로 나옴).
# 게다가 마지막 if문 본문(min 출력)이 빠져 있어서 원래 실행조차 안 됐음.
#
# numbers = list(map(int, input()))
# answer = 0
# chunk = []
# start = numbers[0]
# chunk.append(start)
# numbers.remove(start)
# for num in numbers:
#     if num == start:
#         numbers.remove(num)
#     else:
#         start = num
#         chunk.append(num)
# print(chunk)
# if chunk.count(0) < chunk.count(1):

# --- 다시 짠 버전: 리스트를 건드리지 않고, 바로 이전 값과 비교만 함 ---
numbers = list(map(int, input()))

chunk = [numbers[0]]          # 첫 숫자로 첫 청크 시작
for num in numbers[1:]:
    if num != chunk[-1]:      # 직전 청크와 값이 다르면 새 청크 시작
        chunk.append(num)

answer = min(chunk.count(0), chunk.count(1))
print(answer)
