""" 평균 점수 카운팅
문제 설명
반별 점수가 [국, 영, 수]로 인원만큼 주어집니다. 평균 점수가 80점 이상인 인원이 얼마나 되는지 카운팅하는 solution함수를 완성해주세요.

제한 사항
1 ≤ 학생 수 ≤ 10
0 ≤ 점수 ≤ 100
소숫점 점수는 없습니다.
입출력 예 """

def solution(data):
        
    return len(list(filter( lambda x: x>80 , map(lambda x: sum(x)/3, data))))

data = [[92, 85, 97], [30, 21, 60], [90, 99, 98], [0, 0, 0], [81, 80, 88, 83]]	

print(solution(data))



""" format

def solution(data):
    return None

data =

print(solution(data))
 """