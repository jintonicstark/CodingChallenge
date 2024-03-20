def solution(targets):
    
    targets = sorted(targets)
    
    answer = 1
    aim_start, aim_end = targets.pop(0)
    print(aim_start, aim_end, targets.pop(1))
    count = 0
    for target in targets:
        target_start, target_end = target
        
        if target_start < aim_end:
            aim_start = max(aim_start, target_start)
            aim_end = min(aim_end, target_end)
        else:
            aim_start, aim_end = target_start, target_end
            answer += 1
        count +=1
        print(count, answer, target_start, target_end)

    return answer

data = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	

print(solution(data))