""" 
def solution(data):
    return None

data = 
print(solution(data))

 """


def solution(data):

    prime = [True] * (data + 1)

    prime[0] = prime[1] = False

    for i in range(2, int(data**0.5) + 1):
        if prime[i]:
            for j in range(i * 2, data + 1, i):
                prime[j] = False

    return sum(prime)


def sol2(data):
    prime = [True] * (data + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(data**0.5) + 1):
        if prime[i]:
            for j in range(i * 2, data + 1, i):
                prime[j] = False
    return sum(prime)


data = 10
print(sol2(data))
