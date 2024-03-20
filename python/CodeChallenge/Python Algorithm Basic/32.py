""" 
def solution(data):
    return None

data = 
print(solution(data))

 """

def solution(data):
    sol_and = data[0]
    sol_or = data[0]
    for i in data[1:]:     
        sol_and = sol_and & i
        sol_or = sol_or | i

    return sol_and,sol_or

data = [12, 5, 6]	
print(solution(data))