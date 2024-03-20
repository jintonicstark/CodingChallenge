""" 라이캣은 크리스마스 선물 룰렛 게임을 하고 있습니다. 룰렛에는 '쿠키 1개'부터 '쿠키 10개'까지 값이 들어 있습니다. 룰렛은 총 3번 돌릴 수 있고, 첫번째 시도에서 나온 값은 곱하기 1을 하고, 두번째 시도에서 나온 값은 곱하기 2를 하고 세번째 시도에서 나온 값은 곱하기 3을 하기로 하였습니다. 라이캣이 가져갈 쿠키의 수를 리턴하는 함수를 완성해주세요.

제한 사항
룰렛에는 '쿠키 1개'와 같은 문자열이 주어집니다.
각각의 값은 1차원 리스트로 주어집니다.
중복해서 같은 값을 뽑을 수 있습니다. """

def solution(data):
    sum = 0
    for i,s in enumerate(data):
        print(s.split(" ")[0])
        print(s.split(" ")[1])
        number = int(s.split(" ")[1].replace('개', ''))
        sum += number*i
    return sum

def solution1(data):
    result  = 0
    for i, s in enumerate(data):
    	number  = int(s.split(" ")[1].replace('개', ''))
        result += nmber * (i+1)
    return result

    
data = ['쿠키 3개', '쿠키 2개', '쿠키 5개']	

print(solution(data))

