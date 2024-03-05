"""1의 갯수 반환
문제 설명
주어진 리스트의 값 중 1의 갯수를 반환하는 solution 함수를 완성해주세요.

제한 사항
0 ≤ 리스트의 길이 ≤ 10
1 ≤ 리스트 안의 수 ≤ 10000
들어온 리스트의 값은 정수로 되어 있습니다.
리스트의 길이가 0인경우 0을 반환해주세요."""


def solution(data):
    no1 = 0
    for i in data:
        for s in str(i):
            if s== '1':
                no1 += 1
    return no1


data = [111, 111, 123]


def solution1(data):
    count_of_ones= 0
    for i in data:
        count_of_ones += str(i).count('1')
    return count_of_ones

def solution2(data):
    return(''.join(map(str, data)).count('1'))
print(solution2(data))