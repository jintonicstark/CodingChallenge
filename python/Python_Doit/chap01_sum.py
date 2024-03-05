# a부터 b 까지 정수의 합 구하기

print('a 부터 b 까지의 정수이 합을 구합니다.')
a = int(input('정수 a '))
b = int(input('정수 b '))

if a>b:
    a, b = b, a

sum  = 0 
for i in range(a, b):
    sum += i

print(f'{a}부터 {b} 까지의 정수의 합은 {sum}')