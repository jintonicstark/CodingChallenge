""" format

def solution(data):
    return None

data =

print(solution(data))
 


우편 번호 정렬
문제 설명
각 주소가 담긴 배열과 우편번호 목록이 딕셔너리 형태로 주어질 때 에서 우편번호 오름차순 순서대로 주소를 정렬하는 코드를 작성해주세요.

제한 사항
63002 ≤ 우편번호 ≤ 63364
우편번호는 항상 '시 - 동 - 길' 순으로 주어집니다. 예외사항은 없습니다.
같은 동은 주어지지 않으며, 같은 우편번호도 주어지지 않습니다.
""" 


def solution(data):
    # print(data[1].get(list(data[0])[1].split(' ')[1]))
    return sorted(data[0], key= lambda x: data[1].get(x.split(' ')[1]))

data = [['제주시 A동 한라산길 61', '제주시 B동 백록담길 63', '제주시 C동 사라봉길 31'], {'A동': 63007, 'B동': 63010, 'C동': 63002}]	

print(solution(data))
 

