a,b = map(int,input().split())
c = int(input())

b = b+c
a = a+b//60
b = b%60
if a > 23 :
    a = a-24
print(a, b)