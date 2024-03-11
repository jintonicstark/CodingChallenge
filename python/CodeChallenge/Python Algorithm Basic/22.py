""" format

def solution(data):
    return None

data =
print(solution(data))

"""


def solution(data):
    arr, index = data
    return arr.index(index) if index in arr else False

data = ('hello', 'o')	
print(solution(data))