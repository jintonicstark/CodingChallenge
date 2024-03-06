""" format

def solution(data):
    return None

data =

print(solution(data))

라이캣은 도서관 사서로 일하게 되었습니다. 도서관에 있는 책들의 제목과 해당 책들의 발행 연도가 딕셔너리 형태로 주어집니다. 라이캣을 도와 주어진 책들을 발행 연도가 오래된 순서대로 정렬하는 코드를 작성해주세요. 발행 연도가 같은 경우에는 제목의 사전순으로 정렬하세요.

제한 사항
발행 연도는 1900년부터 2024년 사이입니다.
책 제목은 모두 영문으로 되어 있으며, 대소문자를 구분합니다.
동일한 제목의 책은 존재하지 않습니다.
책의 제목은 공백을 포함할 수 있습니다.
 
""" 


def solution(data):
    books, publish_years = data

    print(list(data[0])[1])

    return sorted(data[0], key= lambda x: (data[1][x], x))

data = [['Moby Dick', 'To Kill a Mockingbird', '1984'], {'Moby Dick': 1851, 'To Kill a Mockingbird': 1960, '1984': 1949}]	

print(solution(data))