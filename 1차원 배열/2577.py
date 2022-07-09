import sys

list_a = [int(sys.stdin.readline()) for i in range(3)]
sum_a = list_a[0]*list_a[1]*list_a[2]

for i in range(10) :
    print(str(sum_a).count(str(i)))
    
