""" 
def solution(data):
    return None

data = 
print(solution(data))

 """


def solution(data):
    binary = bin(data)[2:]
    result = []
    for i in binary:
        if i == '1':
            i = 'A'
        else:
            i = 'B'
        result.append(i)
            
    return ''.join(result)

data = 5
print(solution(data))