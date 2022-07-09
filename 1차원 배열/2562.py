import sys

list_n = []

for i in range(9) : 
    n = int(sys.stdin.readline())
    list_n.append(n)
m = max(list_n)

print(m)
print(list_n.index(m)+1)