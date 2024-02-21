def card_conv(x: int, r: int) -> str:
    d = ''  # 변환된 결과를 저장할 빈 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 각 자릿수에 대응하는 문자들
    
    while x > 0:
        d += dchar[x % r]  # 현재 숫자를 r로 나눈 나머지에 해당하는 문자를 결과 문자열에 추가
        x //= r  # 현재 숫자를 r로 나눈 몫으로 업데이트

    return d[::-1] if d else '0'  # 변환된 결과를 역순으로 반환하고, 결과가 없으면 '0'을 반환

a = int(input('숫자입력'))
b = int(input('진수입력'))

print(f'{card_conv(a,b)}')