# a 부터 b 까지 정수의 합 구하기
import random

a = random.randint(0, 10)
b = random.randint(0, 10)
if a >= b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b:
        print(f"{i}+", end="")
    else:
        print(f"{i}=", end="")
    sum += i

print(sum)
