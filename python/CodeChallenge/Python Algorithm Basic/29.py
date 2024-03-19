""" 
def solution(data):
    return None

data = 
print(solution(data))

""" 

def solution(data):
    result = 0
    for num in  data:
        old_result = result
        result ^= num
        print(f'{old_result}, {num} = {result}')
        print(f'{old_result:b}, {num:b} = {result:b}')
    return result

data = [4, 1, 2, 1, 2]	
print(solution(data))