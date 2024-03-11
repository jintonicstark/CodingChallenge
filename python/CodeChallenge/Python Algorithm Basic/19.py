def solution(data):
    for i in range(len(data)):
        if type(data[i]) ==int:
            data[i] = 'int'
        elif type(data[i]) == float:
            data[i] = 'float'
        elif type(data[i]) == str:
            data[i] = 'str'
        elif type(data[i]) == list:
            data[i] = 'list'
        elif type(data[i]) == tuple:
            data[i] = 'tuple'
        elif type(data[i]) == dict:
            data[i] = 'dict'
        else:
            data[i] = 'bool'
    return data

def solution2(data):
 
    return [type(i).__name__ for i in data]

data = [123, 4.56, "hello", [1, 2, 3], (4, 5), {"a": 1, "b": 2}]
print(solution2(data))
