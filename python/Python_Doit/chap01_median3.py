import random


def median3(a, b, c):
    median = a
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        return c
    if a > c:
        return a
    if b > c:
        return c
    else:
        return b


print("세 정수의 중앙 값을 구한다")


for i in range(10):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    print(f"median3({a},{b},{c}) = {median3(a,b,c)}")
