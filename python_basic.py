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
x = 15
if x>= 10:
    print("X>10")
if x >= 0 :
    print("X >=0")
if x >= 30:
    print("X>=30")

#들여쓰기 Tab vs space
#Python 스타일 가이드라인에서는 4개의 공백 문자를 사용하는것을 표준으로 설정하고 있음

#반복문
#while / for 문이 있지만, for문이 조금더 간결하게 가능

result = 0
for i in range(11):
    result += i
print(result)


for i in range(11):
    if i %2 == 0:
        continue
    result += i
print(result)

for i in range(11):
    if i ==5 :
        break
    print(i)


#함수 및 람다 식
'''
def 함수명(매개변수) :
    실행할 소스코드
    return 반환 값
'''
'''
함수 내에 전역변수 사용하기 위함
global

a= 100
def func():
    global a
    a += 1
    print(a)

fun()
'''
'''
값을 변경 및 변경이 아닌,
값을 참조만 하는 경우에는 그냥 써도 참조됨
// 전역변수로 리스트로 되어있으면, 그냥 써도 됨

'''

'''
함수는 여러개의 반환 값을 가질 수 있음

def operator(a,b) :
    add = a+b
    sub = a-b
    mul = a*b
    di  = a/b
    return add, sub, mul, di

a, b, c, d = operator(7,3)
print(a,b,c,d)
'''
#람다
#함수를 한줄로 작성가능

def add(a,b) :
    return a+b

print(add(3,7))
#람다 함수 == (lambda 식)()
print((lambda a,b: a+b)(3,7))

array = [('홍길동',50), ('이순신',32), ('아무개',74)]

def my_key(x) :
    return x[1]

print(sorted(array, key=my_key))            #sorted(리스트, key속성(정렬기준을 명시 할 수 있음))
print(sorted(array, key=lambda x:x[1]))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b : a+b, list1, list2)        #map = 각각의 원소에 어떤 함수를 적용하려고 할때
print(list(result))             

'''
****************************************************************************
실전에서 유용한 표준 라이브러리

내장함수 : 기본 입출력 함수부터 정렬함수까지 기본적인 함수 제공
- 필수 기능 포함되어있음
itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
- 특히 순열과 조합 라이브러리는 코딩테스트에서 자주 사용됨                  //모든 경우의수 or 완전탐색에서 소스코드를 간결하게 작성하는데 도움됨
heapq : heap 자료구조 제공
- 일반적으로 우선순위 큐 기능을 구현하기 위해 사용                          //최단경로 알고리즘에서 사용됨
bisect : 이진탐색(binary search)기능 제공                               // 기본적인 이진탐색 사용됨
collections : 덱(deque), 카운터(counter) 등의 유용한 자료구조를 포함    
math : 필수적인 수학적 기능 제공
- 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함
****************************************************************************
'''

#자주 사용되는 내장 함수
#sum()                      #//원소들의 합 반환
result = sum([1,2,3,4,5])
print(result)

#min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result,max_result)

#eval()                     #//사람의 입장에서 하나의 식이 있을경우 식을 계산하여 반환함
result = eval("(3+5)*7")
print(result)
print(type(result))

#sorted()
result = sorted([9,1,8,1,5,3,4])    #올림차순
reverse_result = sorted([9,1,8,1,5,3,4], reverse = True)    #내림차순
print(result)
print(reverse_result)

#sorted() with key
array = [('홍길동',50), ('이순신',32), ('아무개',74)]
result = sorted(array, key=lambda x:x[1], reverse = True)   #x[1]가 key값(정렬기준), 내림차순
print(result)

'''
모든 경우의 수를 고려해야 할때 어떤 라이브러리를 효과적으로 사용할 수 있을까요?
순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
- {'A','B','C'}에서 세 개를 선택하여 나열하는 경우: 'ABC','ACB','BAC','CAB','CBA'
조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
- {'A','B','C'}에서 순서를 고려하지 않고 두개를 뽑는 경우 : 'AB','AC','BC'

순열의 수 : nPr = n * (n-1) * (n-2) *...* (n-r+1)
조합의 수 : nCr = { n * (n-1) * (n-2) *...* (n-r+1) } / r!
'''
#순열
# - {'A','B','C'}에서 세 개를 선택하여 나열하는 경우: 'ABC','ACB','BAC','CAB','CBA'
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3))     #튜플로 저장됨
print(result)

###########################################################################
#조합
# - {'A','B','C'}에서 순서를 고려하지 않고 두개를 뽑는 경우 : 'AB','AC','BC'
from itertools import combinations
data = ['A','B','C']
result = list(combinations(data,2))     #튜블로 저장됨
print(result)

#중복 순열과 중복 조합
from itertools import product
data = ['A','B','C']
result = list(product(data, repeat = 2))        #2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

from itertools import combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)
###########################################################################

'''
Counter
파이썬 collections 라이브러리의 Counter는 등장횟수를 세는 기능을 제공합니다.
리스트와 같은 반복 가능한(iterable)객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줍니다.
워드 클라우드와 같은 걸 만들때 매우 유용함
'''
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])  #blue의 등장 횟수 출력
print(counter['green']) #green의 등장 횟수 출력
print(dict(counter))    #사전 자료형으로 반환

###########################################################################
'''
math 라이브러리
원주율과 같은 함수도 포함하고 있음
최대공약수를 구할때는 gcd() 함수
'''
#최소공배를 구하는 함수
import math
def lcm(a,b):
    return a*b // math.gcd(a,b)

a= 21
b= 14

print(math.gcd(21,14))
print(lcm(21,14))

###########################################################################




end_time = time.time()
print("time : ",end_time-start_time)