""" 
def solution(data):
    return None

data = 
print(solution(data))

 """


def solution(data):

    array, k = data
    max_sum = sum(array[:k])
    new_sum = max_sum
    for i in range(len(array) - k):
        new_sum = new_sum - array[i] + array[i+k]
        max_sum = max(new_sum, max_sum)
    return max_sum


data = ([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)

def solution1(data):

    return None
print(solution(data))
