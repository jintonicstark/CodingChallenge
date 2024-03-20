""" 
def solution(data):
    return None

data = 
print(solution(data))

 """
def solution(data):
    binary_str = format(data, '010b')
    invert_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    return     int(invert_str, 2)


def solution1(data):
    binary_str = format(data, '010b')
    inverted_binary_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    return     int(inverted_binary_str)

data = 5

print(solution(data))