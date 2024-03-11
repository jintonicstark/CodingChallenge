""" format

def solution(data):
    return None

data =
print(solution(data))

"""
import time

def solution(data):
    arr, target = data
    print(arr, target)
    for k in range(len(arr)):
        if arr[k] ==target:
            return k
    return False

def sol2(data):
    start_time = time.time_ns()  # 시작 시간 기록 (나노초 단위)

    arr, target = data

    result = arr.index(target) if target in arr else False

    end_time = time.time_ns()  # 종료 시간 기록 (나노초 단위)
    elapsed_time = (end_time - start_time) / 1e6  # 실행 시간 계산 (마이크로초로 변환)
    print(f"Execution time: {elapsed_time:.12f} microseconds")  # 실행 시간 출력

    return result

def sol3(data):
    start_time = time.time_ns()  # 시작 시간 기록 (나노초 단위)

    arr, target = data
    try:
        index = arr.index(target)
        end_time = time.time_ns()  # 종료 시간 기록 (나노초 단위)
        elapsed_time = end_time - start_time  # 실행 시간 계산
        print(f"Execution time: {elapsed_time} seconds")  # 실행 시간 출력
        return index
    except ValueError:
        end_time = time.time_ns()  # 종료 시간 기록 (나노초 단위)
        elapsed_time = end_time - start_time  # 실행 시간 계산
        print(f"Execution time: {elapsed_time} seconds")  # 실행 시간 출력
        return False

 


data = ([1, 3, 5, 7, 9], 5)		
print(sol2(data))
