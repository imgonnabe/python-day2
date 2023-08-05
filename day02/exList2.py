"""
파일명: exList2.py
프로그램 설명: 리스트 자료형에 데이터를 넣는 방법
"""

# 다양한 형태의 리스트 생성 방법
a=[]
b=[1,2,3,4,5]
c=[1.2,3.4,5]
d=['홍길동',"고길동",'김길동']
e=[1,2.5,'홍길동']
f=[1,2.5,['홍길동,2023']]
# f[0]f[1]f[2][0] f[2][1]

# 리스트는 값을 변경할 수 있다.
l = [1,2,3,4,5] 
print(l[0])  # 1

l[0] = 10 # [10,2,3,4,5]
print(l[0])  # 10

# 문자열은 값을 변경할 수 없다.
# 문자열은 값을 변경할 수 없는 불변형 자료형이다.
name = "James"
#       |||||   
#       ||||+-- [4]
#       |||+-- [3]
#       ||+-- [2]
#       |+-- [1]
#       +-- [0]
print(name[0])
name[0] = 'A'