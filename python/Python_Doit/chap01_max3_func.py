# 세 정수의 최댓값 구하기

import random


def max3(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum


for i in range(10):
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    print(f'math3({a}, {b}, {c}) = {max3({a},{b},{c})}')