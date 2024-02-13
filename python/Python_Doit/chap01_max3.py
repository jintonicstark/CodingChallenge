#세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a

if b > maximum: maximum = b
if c > maximum: mximum = c

print(f'최댓값은 {maximum}입니다.')

#test
print('이름을 입력하세요.: ', end='')   #end=''는 줄바꿈을 하지 않는다.
name = input()
print(f'안녕하세요? {name}님.') #f는 format을 의미한다.