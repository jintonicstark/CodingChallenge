""" format

def solution(data):
    return None

data =
print(solution(data))

"""


def solution(data):

    return all([type(instance).__name__ == class_ for class_, instance in data])
data = [('list', [1, 2, 3]), ('int', 4), ('str', 'hello')]	
print(solution(data))
