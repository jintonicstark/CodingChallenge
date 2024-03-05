


def solution(data):

    return list((filter( lambda x: sum(x[1:])>350 ,data)))


data = [['Gray', 98, 92, 85, 97], ['Gom', 98, 30, 21, 60], ['Allosa', 98, 90, 99, 98]]

print(solution(data))