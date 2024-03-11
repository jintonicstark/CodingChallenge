""" def solution(data):
    return None

data = 
print(solution(data))

 """



def solution(data):
    arr, target = data
    return any(target in x for x in arr)

data = ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 7)	
print(solution(data))