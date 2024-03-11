""" format

def solution(data):
    return None

data =
print(solution(data))

"""


def solution(data):
    temp_list = [(data, temp) for temp, data in data.items()]
    temp_list.sort(key=lambda x: (-x[0], x[1]))
    top_tree = temp_list[:3]
    return [f'{temp[2:]}: {data}' for data, temp in top_tree]

data ={'2024-01-01': 15, '2024-01-02': 17, '2024-01-03': 16, '2024-01-04': 20, '2024-01-05': 19, '2024-01-06': 21, '2024-01-07': 18}	
print(solution(data))