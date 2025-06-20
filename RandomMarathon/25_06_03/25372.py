password = []
n = int(input())
for i in range(n):
    password.append(input())

for j in password:
    if 6 <= len(j) <= 9:
        print('yes')
    else:
        print('no')