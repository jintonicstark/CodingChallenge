""" 곱하기
문제 설명
주어진 리스트를 모두 곱하는 solution 함수를 완성해주세요.

제한 사항
1 ≤ 리스트 안의 수 ≤ 100
숫자 외에 다른 값은 주어지지 않습니다.
각각의 값은 1차원 리스트로 주어집니다.
리스트 안에 값이 없는 경우는 0으로 출력해야 합니다.
 """
def solution(data):
    # 초기값을 1로 설정하여 곱셈에 대한 항등원(identity)인 1로 초기화
    if not data:
        return 0
    multi = 1
    for i in data:
        print(multi, i)
        multi *= i  # multi를 i와 곱한 값을 multi에 다시 할당
    return multi


data = [1,3,5,7,9]

print(solution(data))