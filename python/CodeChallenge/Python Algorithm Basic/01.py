#https://100.pyalgo.co.kr/
""" 더하기
문제 설명
주어진 리스트 내에 홀수를 찾아 합을 반환하는 solution 함수를 완성해주세요.

제한 사항
1 ≤ 리스트 안의 수 ≤ 100
숫자 외에 다른 값은 주어지지 않습니다.
각각의 값은 1차원 리스트로 주어집니다.
리스트 안에 값이 없는 경우는 0으로 출력해야 합니다. """

def solution(data):
    return sum(filter(lambda x: x % 2,data))


data = [1,2,3,4,5]
print(list(filter(lambda x: x % 2,data)))
print(solution(data))


def solution(data):
    return sum(filter(lambda x: x%2, data))