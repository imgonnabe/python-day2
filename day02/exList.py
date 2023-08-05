"""
파일명: exList.py
프로그램 설명: 리스트 자료형
"""

# 변수 l에 리스트 형식으로 정수 1 ~ 5까지 저장한다.
l = [1, 2, 3, 4, 5]
print(l, type(l))  # [1, 2, 3, 4, 5] <class 'list'>

# 인덱싱
# 인덱스 번호로 항목을 출력하는 방법
# 형식: 변수명[인덱스번호]
# print(l[2], l[-3])  # 3  --> [2]  [-3] <--
# print(l[0], l[-5])  # 1  --> [0]  [-5] <--
# print(l[4], l[-1])  # 5  --> [4]  [-1] <--

# 멤버쉽 연산
# 종류: in, not in
# in : 값이 있으면 True, 없으면 False
# not in : 값이 없으면 True, 있으면 False
# 연산의 결과 : True, False
# 형식1 : 값 in 변수명
# 형식2 : 값 in 값
# 형식3 : 변수명 in 변수명
# 형식4 : 변수명 in 값

# l변수에 2가 존재합니까 ?
# print(2 in l)      # True
# l변수에 7이 존재하지 않습니까 ?
# print(7 not in l)  # True

# 크기 함수
# 크기 함수를 이용해서 자료의 길이(개수)를 확인할 수 있다.
# 리스트에서 크기 함수를 사용하면 항목의 개수를 구한다.
# 형식 : 함수명(인수),  len(변수명)
# 리턴값 : 변수의 개수
# 인수 : 입력값, 리턴값 : 출력값
# print(len(l))  # 5

# 슬라이싱
# 슬라이싱 : 범위를 지정해서 데이터를 추출하는 기법이다.
# 형식 : 변수명[시작숫자:끝숫자]
# 여기서 시작숫자와 끝숫자는 index 번호를 의미한다.
# 범위 : 시작숫자 ~ 끝숫자 -1 까지
# 시작숫자 생략 : 처음부터
# 끝숫자 생략 : 시작숫자 ~ 끝까지
print(l[1:3],l[-4:-2])
print(l[2:],l[-3:])

# 반복성 (Iterable)
# 반복할 때 사용하는 형식 : 제어문을 사용한다.
# 제어문은 프로그램의 흐름을 제어할 때 사용한다.
# for문
# 형식 : 
# for 변수 in 리스트:
#     실행문1
# else:
#     실행문2

# for문을 이용해서 l변수에 저장된 1 ~ 5까지 출력하기
# for value in l:
#     print(value)
# else:
#     print('for문 종료')
for a in l:
    print(f'2 x {a} = {2*a}')
else:
    print('for문 종료')

print(l +[10,20,30,40,50])
print(l)
l+=[10,20,30,40,50]
print(l)