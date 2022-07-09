c =int(input())

for i in range(c) :
    n = list(map(int,input().split()))
    N = n.pop(0)
    temp = sum(n)/N
    Mean = list(filter(lambda x: x>temp, n))
    temp = len(Mean)/N*100
    print('%.3f'%temp,'%',sep="")