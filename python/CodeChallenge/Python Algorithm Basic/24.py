""" def solution(data):
    return None

data = 
print(solution(data))

 """


def solution(data):
    result =  -float("inf")  
    for i in data:
        print(data[i], data[next(i)])
    return None

data = [1, -2, 3, 4, -1, 2, 1, -5, 4]	
print(solution(data))

