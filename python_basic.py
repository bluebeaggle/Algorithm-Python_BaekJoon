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







end_time = time.time()
print("time : ",end_time-start_time)