# 입력받은 정수의 부호 (양수, 음수, 0) 출력하기

import random



def floatDef (n):
    if n == 0: return('정수의 부호는 0')
    if n > 0: return('정수의 부호는 +')
    if n < 0: return('정수의 부호는 -')

for i in range(10):
    a  = random.randint(-10,10)
    print(f'{a}는 {floatDef(a)}')

