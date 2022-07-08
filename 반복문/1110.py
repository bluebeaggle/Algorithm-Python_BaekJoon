a = int(input())
i = 0
b = a
while True :
    a = a%10*10+(a//10+a%10)%10
    i +=1
    if a == b :
        break
print(i)