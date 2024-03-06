""" format

def solution(data):
    return None

data =

print(solution(data))
문제 설명
도서관의 책들은 각각 고유한 위치 코드를 가지고 있습니다. 책의 위치 코드와 해당 위치 코드에 대응하는 책의 제목이 딕셔너리 형태로 주어질 때, 위치 코드 순으로 책의 제목을 정렬하는 코드를 작성해주세요. 위치 코드는 문자열로 구성되며, 사전순으로 정렬합니다.

제한 사항
위치 코드는 영문 대소문자와 숫자로 구성된 문자열입니다.
위치 코드의 길이는 최대 10자입니다.
도서관에는 최소 1권에서 최대 100권의 책이 있습니다.
같은 위치 코드를 가진 책은 없습니다.

 
"""


def solution(data):
    result_set = []
    for i in range(len(data)):
        print(data[sorted(list(data))[i]])
        result_set.append(data[sorted(list(data))[i]])

    return result_set


def solution1(data):
    result_set = sorted(data.keys())
    return [data[i] for i in result_set]
data = {"AX21": "Moby Dick", "BX32": "1984", "CX14": "To Kill a Mockingbird"}

print(solution1(data))
