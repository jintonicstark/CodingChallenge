def is_valid(s):
    stack = []
    print(stack)
    for char in s:
        print(stack)
        if stack and stack[-1] == '[' and char ==']':
            del stack[-1]
        elif  stack and stack[-1] == '{' and char =='}':
            del stack[-1]
        elif  stack and stack[-1] == '(' and char ==')':
            del stack[-1]
        else:
            stack.append(char)
    return stack == []
def solution(s):
    answer = 0
    for x in range(len(s)):
        
        if is_valid(s[x:]+s[:x]):
            answer +=1
    return answer

data = "[](){}"	

print(solution(data))