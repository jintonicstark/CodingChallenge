# 각 배열의 원소의 최댓값을 구해서 출력하기 ( 튜플, 튜플 문자열 리스트)

from chap02_max import max_of

t = (4,5,5213,32,4,3,1)
s = 'string'
a = ['DTS','AAA','FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')