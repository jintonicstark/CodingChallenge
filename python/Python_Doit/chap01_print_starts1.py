# *을 n개 출력되게 하되 w 개마다 줄바꿈

a = int(input('별 개수를 입력하세요 : '))
b = int(input('줄바꿀 수를 입력하세요:'))

for i in range(a):
    print('*', end='')
    if i%b == b-1:
        print()