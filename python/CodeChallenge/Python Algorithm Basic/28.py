""" 
def solution(data):
    return None

data = 
print(solution(data))

 """


def solution(data):

    nums, target = data
    closset_sum = float("inf")
    left, right = 0, len(nums) -1

    while left < right:
        current_sum =  nums[left] + nums[right]
        if abs(target - current_sum) < abs(target - closset_sum):
            closset_sum = current_sum
        if current_sum < target:
            left +=1
        else :
            right -=1

    return closset_sum

data = ([1, 2, 3, 4, 5], 10)	
print(solution(data))
