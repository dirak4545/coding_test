import sys

print(sys.float_info.epsilon)

a = 0.1 + 0.1 + 0.1
b = 0.3

print(a - b)
if abs(a - b) < sys.float_info.epsilon:
    print("a == b")
else:
    print("a != b")

#