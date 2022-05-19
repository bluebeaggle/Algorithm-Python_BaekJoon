from re import A
import time

start_time = time.time()
# int
a = 1000
print(a)
print(type(a))
#float          ##4byte or 8byte 
a = 1.001
print(a)
a= 1.
print(a)
a = .7
print(a)
#round Function 
a = 123.456
print(round(a,2))
# e (float) 
a = 1e2
print(a)
a = 75.25e1
print(a)
a = 3954e-3
print(a)
a = int(1e2)
print(a)

#list comprehension
a = [i for i in range(10)]
print(a)
a = [i*i for i in range(1,10)]
print(a)
a = [i for i in range(20) if i%2 ==0]
print(a)
# 2nd Demension ## NxM 
n=2;m=3
a = [[0]*m for _ in range(n)]  
print(a)

#특정값 all remove in list
a = [1,2,3,4,5,6,5,5,5,5]
remove_set = {3,5}  #set
result = [i for i in a if i not in remove_set]
print(result)


#집합 자료형의 연산 (Set)
a= set([1,2,3,4,5])
b= set([3,4,5,6,7])

#합집합
print(a|b)
#교집합
print(a&b)
#차집합
print(a-b)

#집합 자료형 관련 함수
data = set([1,2,3])
print(data)
#원소추가
data.add(4)
print(data)
#새로운 원소 여러 개 추가
data.update([5,6])
print(data)
#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)




#사전 자료형과 집합 자료형의 특징
'''
리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
사전 자료형과 집합 자료형은 순서가 없기때문에 인덱싱으로 값을 얻을 수 없다.
* 사전의 키(key) 혹은 집합의 원소(elemnet)를 이용해 O(1)의 시간 복잡도로 조회가능
'''

#기본 입출력
'''
자주 사용되는 표준 입력 방법
- input() - 한줄의 문자열을 입력 받는 함수
- map() - 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
예시 ) 공백을 기준으로 구분된 데이터를 입력받을 때는 다음과 같이 사용
--- list(map(int, input(),split()))
예시 ) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용한다
--- a, b, c = map(int,input().split())
'''
'''
*****많이 쓰임******
데이터의 개수 입력
n = int(input())
각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int,input().split()))

data = sort(reverse = True)
print(data)

***********빠르게 입력 받기************//입력을 받는 시간이 너무 길어 시간초과 되는 경우도 있음
sys 라이브러리 함수
sys.stdin.readline() 메서드 사용 가능
단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용함 // 오른쪽에 붙은 기호는 제거

data = sys.stdin.readline().rstrip()

'''

'''
표준 출력 함수
print()함수 사용
 각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분 가능
 + 연산은 같은 속성(문자열, 정수형)으로만 가능하다
print()는 기본적으로 출력 이후에 줄 바꿈을 수행한다
줄 바꿈을 원치 않는 경우 'end'속성 이용

print(7, end = " ")
print(9, end = " ")
'''

'''
f-string 예제
파이썬 3.6부터 사용가능하며, 문자열 앞에 접두사 'f'를 붙여 사용
중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있음

answer = 7
print(f"정닶은 {answer}입니다. ")
'''


#조건문과 반복문
#part1 - 조건문






































end_time = time.time()
print("time : ",end_time-start_time)