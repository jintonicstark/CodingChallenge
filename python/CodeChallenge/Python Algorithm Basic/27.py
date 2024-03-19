""" 
def solution(data):
    return None

data = 
print(solution(data))

 """


def solution(data):

    nums, target = data
    min_length = float("inf")
    window_sum = 0
    window_start = 0
    for window_end in range(len(nums)):
        window_sum += nums[window_end]

        while window_sum >= target:
            min_length = min(min_length, window_end-window_start+1)
            window_sum -= nums[window_start]
            window_start += 1
    return min_length if min_length != float("inf") else 0



    return None

data = ([2, 1, 5, 2, 3, 2], 7)	
print(solution(data))
