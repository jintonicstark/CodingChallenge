""" A 문자열 덧셈
문제 설명
주어진 문자열의 숫자를 모두 더하는 solution 함수를 완성해주세요.

제한 사항
0 ≤ 리스트의 안의 숫자 ≤ 9
숫자가 연달아 있는 경우에는 한 자리씩 잘라내어 더합니다.
문자열 안에는 숫자와 문자가 조합되어 있습니다.
문자열 길이가 0인 경우에는 0을 반환해주세요.
a"""  """ """

def solution(data):
    sol = 0
    for char in data:
        if char.isdigit():
            sol += int(char)
    return sol

def solution1(data):
    return sum(map(int, filter(str.isdigit, data)))

data ='1hel2lo3'

print(solution1(data))