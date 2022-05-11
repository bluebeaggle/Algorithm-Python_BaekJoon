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







end_time = time.time()
print("time : ",end_time-start_time)