""" 
def solution(data):
    return None

data = "항상 여기로 연락주세요 01012345678."	
print(solution(data))

 """
# 항상 여기로 연락주세요 "Contact me at 010-1234-5678."


def solution(data):
    import re
    pattern = r'(\d{3})(\d{3,4})(\d{4})'

    return re.sub(pattern, r'\1-\2-\3', data)

data = "항상 여기로 연락주세요 01012345678."	
print(solution(data))