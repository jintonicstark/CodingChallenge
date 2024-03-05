# 1부터 n 까지 더하기


def sum_while(n):
    a = 4
    for i in range(n):
        a+=i
        print(a)
    return a

print(f'n 까지 더하기 {sum_while(4)}')