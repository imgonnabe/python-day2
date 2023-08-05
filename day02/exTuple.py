"""
파일명: exTuple.py
프로그램 설명: 튜플 자료형
"""

# 튜플은 리스트와 동일한 특징을 가지고 있다.
# 인덱스, 멤버쉽 연산, 크기 함수, 슬라이싱, 반복성, + 연산자, * 연산자
# 여기서는 아래에는 인덱싱, 반복성, + 연산자, * 연산자만 사용한다.

# 변수 t에 튜플 형식으로 정수 1 ~ 5까지 저장한다.
#    +-- t[-5]
#    |  +-- t [-4]
#    |  |  +-- t[-3]
#    |  |  |  +-- t[-2]
#    |  |  |  |  +-- t[-1]
#    |  |  |  |  |
t = (1, 2, 3, 4, 5)
#    |  |  |  |  |
#    |  |  |  |  +-- t[4]
#    |  |  |  +-- t[3]
#    |  |  +-- t[2]
#    |  +-- t[1]
#    +-- t[0]
print(t,type(t))

# 인덱싱
# 인덱스 번호로 항목을 출력하는 방법
# 형식: 변수명[인덱스번호]
print(t[2],t[-3])
print(t[0],t[-5])
print(t[4],t[-1])

# 멤버쉽 연산
# 종류: in, not in
# in : 값이 있으면 True, 없으면 False
# not in : 값이 없으면 True, 있으면 False
# 연산의 결과 : True, False
# 형식1 : 값 in 변수명
# 형식2 : 값 in 값
# 형식3 : 변수명 in 변수명
# 형식4 : 변수명 in 값
print(2 in t)
print(7 not in t)

# 크기 함수
# 크기 함수를 이용해서 자료의 길이(개수)를 확인할 수 있다.
# 튜플에서 크기 함수를 사용하면 항목의 개수를 구한다.
# 형식 : 함수명(인수),  len(변수명)
# 리턴값 : 변수의 개수
# 인수 : 입력값, 리턴값 : 출력값
print(len(t))

# 슬라이싱
# 슬라이싱 : 범위를 지정해서 데이터를 추출하는 기법이다.
# 형식 : 변수명[시작숫자:끝숫자]
# 여기서 시작숫자와 끝숫자는 index 번호를 의미한다.
# 범위 : 시작숫자 ~ 끝숫자 -1 까지
# 시작숫자 생략 : 처음부터
# 끝숫자 생략 : 시작숫자 ~ 끝까지
print(t[1:3],t[-4:-2])
print(t[2:],t[-3:])
print(t[:3],t[:-2])

# 반복성 (Iterable)
# 반복할 때 사용하는 형식 : 제어문을 사용한다.
# 제어문은 프로그램의 흐름을 제어할 때 사용한다.
# for문
# 형식 : 
# for 변수 in 튜플:
#     실행문1
# else:
#     실행문2

t=(1,2,3,4,5,6,7,8)
for value in t:
    print(f'2 x {value} = {value*2}')
else:
    print('for문 종료')

# 인덱스 값 변경 X
# 단 편법으로 값을 새롭게 만들어서 t 변수에 저장할 수 있다.
t = (1,2,3,4,5)
# t[0] = 100  # 에러 (수정 X)

